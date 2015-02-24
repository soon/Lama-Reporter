# coding=utf-8
"""
This module defined class for Lama Bot
"""
from itertools import imap, ifilter
import json
import mimetypes
import os
import string
from threading import Thread, Event
import time
import logging
import re

import requests
from pymorphy2 import MorphAnalyzer

from lama_beautifier import LamaBeautifier
from thread_safe_vk import ThreadSafeVkApi
from utils import safe_call_and_log_if_failed
from vk_message import VkMessage
from vk_objects import VkPhoto, VkDocument, VkUser


__all__ = ['LamaBot']


class LamaBot(object):
    def __init__(self, app_id, mail_manager,
                 chat_id=1, number_of_seconds_for_the_rest=60, chat_id_for_mails=None, admins=None, **kwargs):
        """
        Initializes Lama Bot.

        Expects login/password or access_token as named parameters

        :param mail_manager: A manager for retrieving mails
        :type mail_manager: AbstractMailManager

        :param chat_id: Chat identifier
        :type chat_id: int

        :param chat_id_for_mails: Chat for mails. Same as chat_id, if not presented
        :type chat_id_for_mails: int

        :raise ValueError: When neither login/password nor access_token was provided
        """
        self.exit_event = Event()
        self.morph = MorphAnalyzer()
        self.version = '0.1.1'
        self.app_id = app_id
        self.access_token = None
        self.password = None
        self.login = None
        self.vkapi = ThreadSafeVkApi(app_id=app_id, **kwargs)
        self.commands = {}
        self._plugins = []
        self.mail_manager = mail_manager
        self.number_of_seconds_for_the_rest = number_of_seconds_for_the_rest
        self.chat_id = chat_id
        self.chat_id_for_mails = chat_id_for_mails or self.chat_id
        self.admins = admins or []

        self.initialize_commands()

    def initialize_commands(self):
        self.commands = {
            'post_to_dialog': self.safe_post_message_and_log_if_failed
        }

    def safe_notify_about_unread_mails(self):
        for m in self.safe_unread_mails:
            if self.safe_post_mail_and_log_if_failed(m):
                self.mail_manager.safe_mark_mail_as_read_and_log_if_failed(m)

    def safe_process_directed_dialog_message(self, message):
        logging.debug(u'Processing message with body {}'.format(message.body))
        words = self.split_to_words(message.body)
        logging.debug(u'Words in the body: {}'.format(words))
        self.safe_process_plugins(message, words)
        self.safe_mark_message_as_read_and_log_if_failed(message)

    def safe_process_private_message(self, message):
        if self.safe_execute_and_log_if_failed(message.body):
            self.safe_mark_message_as_read_and_log_if_failed(message)

    @safe_call_and_log_if_failed
    def safe_process_plugins(self, message, words):
        normalized_words = self.normalize_words(words)
        for p in self.plugins:
            p.process_input(message.body, words, normalized_words, message)

    def long_pool_loop(self, exit_event):
        server, key, ts = self.extract_server_key_and_timestamp_from_get_long_poll_server_response()

        while not exit_event.is_set():
            response = self.send_long_poll_request(server, key, ts)
            if 'failed' in response:
                server, key, ts = self.extract_server_key_and_timestamp_from_get_long_poll_server_response()
            else:
                self.process_long_poll_response(response)
                ts = self.get_timestamp(response, ts)

    def extract_server_key_and_timestamp_from_get_long_poll_server_response(self):
        response = self.vkapi.messages_get_long_poll_server()
        while not all(x in response for x in ('server', 'key', 'ts')):
            logging.error('Could not retrieve credentials for connecting to long poll server', response)
            self.post_message_to_admins('Could not retrieve credentials for connecting to long poll server')
            response = self.vkapi.messages_get_long_poll_server()
        return response['server'], response['key'], response['ts']

    @safe_call_and_log_if_failed(default={})
    def send_long_poll_request(self, server, key, ts, act='a_check', wait=25, mode=2):
        params = {
            'act': act,
            'key': key,
            'ts': ts,
            'wait': wait,
            'mode': mode
        }
        return requests.get('http://{server}'.format(server=server), params=params).json()

    def process_long_poll_response(self, response):
        if response:
            for update in response.get('updates', []):
                self.process_long_poll_update(update)

    def process_long_poll_update(self, update):
        functions = {
            4: self.process_long_poll_new_message
        }
        function = functions.get(update[0])
        if function:
            function(update)

    def process_long_poll_new_message(self, update):
        chat_id = self.get_chat_id_from_long_poll_new_message_update(update)
        fwd_messages = self.get_fwd_messages_from_long_poll_new_message_update(update)
        self.process_new_message(VkMessage({'id': update[1],
                                            'user_id': None,
                                            'read_state': (update[2] + 1) % 2,
                                            'chat_id': chat_id,
                                            'title': update[5],
                                            'body': update[6],
                                            'fwd_messages': fwd_messages}))

    def process_new_message(self, message):
        if message.is_unread:
            if message.chat_id == self.chat_id and self.message_is_directed(message):
                self.safe_process_directed_dialog_message(message)
            elif message.is_private:
                self.safe_process_private_message(message)

    def get_fwd_messages_from_long_poll_new_message_update(self, update):
        return map(self.convert_fwd_from_long_poll_new_message_update_to_fwd_message,
                   ifilter(None,
                           self.get_attachments_from_long_poll_new_message_update(update).get('fwd', '').split(',')))

    @staticmethod
    def convert_fwd_from_long_poll_new_message_update_to_fwd_message(fwd):
        regex = re.compile('(?P<user_id>\d+)_(?P<msg_id>\d+)')
        m = regex.match(fwd)
        return {
            'id': m.group('msg_id'),
            'user_id': m.group('user_id')
        }

    @staticmethod
    def get_chat_id_from_long_poll_new_message_update(update):
        """
        The message was sent from chat if user_id is greater than 2000000000
        :param update:
        :return:
        """
        return update[3] - 2000000000 if update[3] > 2000000000 else None

    def get_user_id_from_long_poll_new_message_update(self, update):
        """
        Retrieves user_id from update according to documentation
        https://vk.com/pages?oid=-17680044&p=Connecting_to_the_LongPoll_Server
        :param update:
        :return:
        """
        return self.get_attachments_from_long_poll_new_message_update(update).get('from')

    @staticmethod
    def get_attachments_from_long_poll_new_message_update(update):
        return update[7] if len(update) > 7 else {}

    @staticmethod
    def get_timestamp(response, default):
        return response.get('ts', default) if response else default

    @property
    def unread_mails(self):
        return self.mail_manager.unread_mails

    @property
    def safe_unread_mails(self):
        """
        Just delegates the work to the mail manager
        :return:
        """
        return self.mail_manager.safe_unread_mails

    @property
    def vkapi_messages_get(self):
        return self.vkapi.messages_get()

    @property
    def plugins(self):
        """

        :rtype : a list of LamaPlugin
        """
        return self._plugins

    def vkapi_messages_set_activity_in_chat(self):
        return self.vkapi.messages_set_activity(chat_id=self.chat_id, type='typing')

    def post_mail(self, mail):
        """
        Posts mail to VK. Loads and attaches documents, if any.
        :param mail:
        :return:
        """
        documents = None
        if mail.attachments:
            documents = filter(None, imap(self.safe_upload_attachment, mail.attachments))
        self.post_message_to_mail_dialog(self.wrap_mail(mail), attachments=documents)

    @safe_call_and_log_if_failed(default=False)
    def safe_post_mail_and_log_if_failed(self, mail):
        """
        :param mail:
        :return: True if no error, False otherwise
        """
        self.post_mail(mail)
        return True

    @safe_call_and_log_if_failed()
    def safe_post_message_and_log_if_failed(self, message):
        self.post_message_to_dialog(message)

    @safe_call_and_log_if_failed
    def safe_post_message_with_forward_messages(self, message, forward_messages):
        self.post_message_to_dialog(message, forward_messages=forward_messages)

    def execute(self, s):
        command, args = self.split_to_command_and_argument(s)
        if command in self.commands:
            self.commands[command](args)
        else:
            self.command_not_found(command)

    @safe_call_and_log_if_failed(default=False)
    def safe_execute_and_log_if_failed(self, s):
        self.execute(s)
        return True

    @staticmethod
    def split_to_command_and_argument(command):
        values = command.split(':', 1)
        if len(values) != 2:
            values.append(None)
        return values[0], values[1]

    def _post_message_to_dialog(self, chat_id, message, attachments=None, forward_messages=None):
        """
        Posts message to dialog. Attaches attachments, if any.
        :param forward_messages: Messages to be forwarded
        :type forward_messages: [VkMessage]
        :param attachments:Documents to be attached
        :type attachments: [VkDocument]
        :param message:
        """
        attachments = attachments or []
        forward_messages = forward_messages or []
        attachment = ','.join(map(lambda d: d.attachment_string, attachments))
        forward_messages_str = ','.join(map(lambda m: str(m.id), forward_messages))
        self.vkapi.messages_send(chat_id=chat_id,
                                 message=message,
                                 attachment=attachment,
                                 forward_messages=forward_messages_str)

    def post_message_to_dialog(self, message, attachments=None, forward_messages=None):
        self._post_message_to_dialog(self.chat_id, message, attachments=attachments, forward_messages=forward_messages)

    def post_message_to_mail_dialog(self, message, attachments=None, forward_messages=None):
        self._post_message_to_dialog(self.chat_id_for_mails, message,
                                     attachments=attachments, forward_messages=forward_messages)

    def post_startup_message_to_admins(self):
        self.post_message_to_admins('The Lama is ready to work! (version {0})'.format(self.version))

    @safe_call_and_log_if_failed
    def post_message_to_admins(self, message):
        for user_id in self.admins:
            self.vkapi.messages_send(user_id=user_id, message=message)

    def command_not_found(self, command):
        message = u'Command `{}` not found'.format(command)
        logging.warning(message)

    def run(self, post_welcome_message_to_dialog=True):
        if post_welcome_message_to_dialog:
            self.post_startup_message_to_admins()

        long_poll = Thread(target=self.long_pool_loop, args=(self.exit_event,))
        long_poll.start()

        while True:
            self.safe_notify_about_unread_mails()
            time.sleep(self.number_of_seconds_for_the_rest)

    def stop_running(self):
        self.exit_event.set()

    @safe_call_and_log_if_failed
    def safe_upload_attachment(self, attachment):
        """
        Uploads given attachment

        :type attachment: Attachment
        :rtype: VkDocument
        """
        if attachment.is_loaded:
            url = self.safe_docs_get_upload_server()
            file_string = self.safe_upload_file_to_server(url, self.create_attachment_filename(attachment.filename),
                                                          attachment.data, attachment.mime_type)
            return self.safe_save_doc_file(file_string, attachment.filename)

    @safe_call_and_log_if_failed
    def safe_upload_message_photo(self, image_file_path):
        if image_file_path is not None:
            url = self.safe_get_upload_server_for_private_message_photo()
            data = self.safe_upload_photo_to_server(url, self.create_attachment_filename(image_file_path),
                                                    self.get_image_data(image_file_path),
                                                    self.get_mime_type(image_file_path))
            photo_name = os.path.basename(image_file_path)
            return self.safe_save_photo_file(data['photo'], data['server'], data['hash'], photo_name)

    @staticmethod
    def get_image_data(image_filename):
        with open(image_filename, 'rb') as f:
            data = f.read()
        return data

    @staticmethod
    def get_mime_type(image_filename):
        return mimetypes.guess_type(image_filename)

    @safe_call_and_log_if_failed
    def safe_save_photo_file(self, photo, server, hash, title):
        if photo:
            responses = self.vkapi.photos_save_message_photo(photo=photo, server=server, hash=hash, title=title)
            return VkPhoto(responses[0])

    @safe_call_and_log_if_failed
    def safe_get_upload_server_for_private_message_photo(self):
        """
        Retrieves upload_url for storing files
        """
        return self.vkapi.photos_get_messages_upload_server()['upload_url']

    @staticmethod
    def create_attachment_filename(filename):
        _, extension = os.path.splitext(filename)
        return 'attachment' + extension

    @safe_call_and_log_if_failed
    def safe_upload_to_server(self, url, filename, data, mime_type, post_name):
        """
        Uploads data to given url and saves it with given filename and mime_type

        :return: Raw response, returned by post request
        """
        if url:
            request = requests.post(url, files={post_name: (filename or 'NoName', data, mime_type)})
            response = json.loads(request.text)
            if 'error' in response:
                raise Exception(response['error'])
            else:
                return response

    def safe_upload_file_to_server(self, url, filename, data, mime_type):
        return self.safe_upload_to_server(url, filename, data, mime_type, 'file')['file']

    def safe_upload_photo_to_server(self, url, filename, data, mime_type):
        return self.safe_upload_to_server(url, filename, data, mime_type, 'photo')

    @safe_call_and_log_if_failed
    def safe_save_doc_file(self, file_string, title):
        """
        Saves file on VK server by given string

        :param file_string: String, returned after uploading file
        :return: Saved document
        :rtype: VkDocument
        """
        if file_string:
            responses = self.vkapi.docs_save(file=file_string, title=title)
            return VkDocument(responses[0])

    @safe_call_and_log_if_failed
    def safe_docs_get_upload_server(self):
        """
        Retrieves upload_url for storing files
        """
        return self.vkapi.docs_get_upload_server()['upload_url']

    def retrieve_users_by_ids(self, *user_ids):
        return map(VkUser, self.vkapi.users_get(user_id=','.join(imap(str, user_ids))))

    @staticmethod
    def wrap_mail(mail):
        return LamaBeautifier.get_random_mail_pattern().format(subject=mail.subject, sender=mail.sender, body=mail.body)

    @staticmethod
    def message_is_directed(message):
        return message.body is not None and message.body.encode('utf-8').startswith('Лама, ')

    @staticmethod
    def message_has_body(message):
        return message.body is not None

    def mark_message_as_read(self, message):
        self.mark_message_as_read_by_id(message.id)

    @safe_call_and_log_if_failed(default=False)
    def safe_mark_message_as_read_and_log_if_failed(self, message):
        self.mark_message_as_read(message)
        return True

    def mark_message_as_read_by_id(self, message_ids):
        self.vkapi.messages_mark_as_read(message_ids=message_ids)

    def register_plugin(self, plugin):
        self._plugins.append(plugin)
        plugin.bot = self

    def split_to_words(self, body):
        return body.encode('utf-8').translate(string.maketrans('', ''), string.punctuation).split()

    def normalize_words(self, words):
        return map(self.normalize_word, words)

    def normalize_word(self, word):
        return self.morph.parse(word.decode('utf8'))[0].normal_form.encode('utf8')