# coding=utf-8
"""
This module defined class for Lama Bot
"""
from itertools import imap, ifilter
import json
import os
import string
import time
import logging

import requests
import vk

from lama.vk_document import VkDocument
from lama_beautifier import LamaBeautifier
from utils import safe_call_and_log_if_failed
from vk_message import VkMessage


__all__ = ['LamaBot']


class LamaBot(object):
    def __init__(self, app_id, mail_manager, chat_id=1, number_of_seconds_for_the_rest=60, **kwargs):
        """
        Initializes Lama Bot.

        Expects login/password or access_token as named parameters

        :param mail_manager: A manager for retrieving mails
        :type mail_manager: AbstractMailManager

        :param chat_id: Chat identifier
        :type chat_id: int

        :raise ValueError: When neither login/password nor access_token was provided
        """
        self.version = '0.1.1'
        self.app_id = app_id

        self.access_token = None
        self.password = None
        self.login = None
        self.vkapi = None
        self.commands = {}
        self._plugins = []

        self.initialize_commands()

        self.mail_manager = mail_manager
        self.number_of_seconds_for_the_rest = number_of_seconds_for_the_rest

        if 'login' in kwargs and 'password' in kwargs:
            self.login, self.password = kwargs['login'], kwargs['password']
        elif 'access_token' in kwargs:
            self.access_token = kwargs['access_token']
        else:
            raise ValueError('Expected login/password or access_token parameter')

        self.chat_id = chat_id

    def initialize_vkapi(self):
        if self.login and self.password:
            self.vkapi = vk.API(self.app_id, self.login, self.password)
        elif self.access_token:
            self.vkapi = vk.API(access_token=self.access_token)
        else:
            raise ValueError('Either login/password or access_token are not initialized')

    def initialize_commands(self):
        self.commands = {
            'post_to_dialog': self.safe_post_message_and_log_if_failed
        }

    def safe_notify_about_unread_mails(self):
        for m in self.safe_unread_mails:
            if self.safe_post_mail_and_log_if_failed(m):
                self.mail_manager.safe_mark_mail_as_read_and_log_if_failed(m)

    def safe_check_private_messages(self):
        for m in filter(lambda x: x.body is not None, self.safe_unread_private_messages):
            if self.safe_execute_and_log_if_failed(m.body):
                self.safe_mark_message_as_read_and_log_if_failed(m)

    def safe_process_dialog_messages(self):
        for m in self.safe_directed_unread_dialog_messages:
            logging.debug(u'Processing message with body {}'.format(m.body))
            words = self.split_to_words(m.body)
            logging.debug(u'Words in the body: {}'.format(words))
            self.safe_process_plugins(m, words)
            self.safe_mark_message_as_read_and_log_if_failed(m)

    @safe_call_and_log_if_failed
    def safe_process_plugins(self, message, words):
        for p in self.plugins:
            p.process_input(message.body, words, message)

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
    def safe_directed_unread_dialog_messages(self):
        """
        Filters messages, sent directly to Lama
        :return:
        """
        return self.ifilter_directed_messages(self.safe_unread_dialog_messages)

    @property
    def safe_unread_dialog_messages(self):
        return self.ifilter_unread_messages(self.safe_dialog_messages_iter)

    @property
    def unread_private_messages(self):
        return self.ifilter_unread_messages(self.private_messages_iter)

    @property
    def safe_unread_private_messages(self):
        return self.ifilter_unread_messages(self.safe_private_messages_iter)

    @property
    def private_messages_iter(self):
        return self.ifilter_private_messages(self.messages_iter)

    @property
    def safe_dialog_messages_iter(self):
        return self.ifilter_dialog_messages(self.safe_messages_iter)

    @property
    def safe_private_messages_iter(self):
        return self.ifilter_private_messages(self.safe_messages_iter)

    @property
    def messages_iter(self):
        return imap(VkMessage, self.raw_messages)

    @property
    def safe_messages_iter(self):
        return imap(VkMessage, self.safe_get_raw_messages_and_log_if_failed)

    @property
    def raw_messages(self):
        self.initialize_vkapi()
        response = self.vkapi.messages.get()
        return response.get('items', [])

    @property
    @safe_call_and_log_if_failed(default=[])
    def safe_get_raw_messages_and_log_if_failed(self):
        return self.raw_messages

    @property
    def plugins(self):
        """

        :rtype : a list of LamaPlugin
        """
        return self._plugins

    def post_mail(self, mail):
        """
        Posts mail to VK. Loads and attaches documents, if any.
        :param mail:
        :return:
        """
        documents = None
        if mail.attachments:
            documents = filter(None, imap(self.safe_upload_attachment, mail.attachments))
        self.post_message_to_dialog(self.wrap_mail(mail), documents=documents)

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

    def post_message_to_dialog(self, message, documents=None, forward_messages=None):
        """
        Posts message to dialog. Attaches documents, if any.
        :param forward_messages: Messages to be forwarded
        :type forward_messages: [VkMessage]
        :param documents:Documents to be attached
        :type documents: [VkDocument]
        :param message:
        """
        self.initialize_vkapi()
        documents = documents or []
        forward_messages = forward_messages or []
        attachment = ','.join(map(lambda d: d.attachment_string, documents))
        forward_messages_str = ','.join(map(lambda m: str(m.id), forward_messages))
        self.vkapi.messages.send(chat_id=self.chat_id,
                                 message=message,
                                 attachment=attachment,
                                 forward_messages=forward_messages_str)

    def post_welcome_message(self):
        self.safe_post_message_and_log_if_failed('The Lama is ready to work! (version {0})'.format(self.version))

    def command_not_found(self, command):
        message = u'Command `{}` not found'.format(command)
        logging.warning(message)

    def run(self, post_welcome_message_to_dialog=True):
        if post_welcome_message_to_dialog:
            self.post_welcome_message()

        while True:
            self.safe_notify_about_unread_mails()
            self.safe_check_private_messages()
            self.safe_process_dialog_messages()
            time.sleep(self.number_of_seconds_for_the_rest)

    @safe_call_and_log_if_failed
    def safe_upload_attachment(self, attachment):
        """
        Uploads given attachment

        :type attachment: Attachment
        :rtype: VkDocument
        """
        if attachment.is_loaded:
            url = self.safe_docs_get_upload_server()
            file_string = self.safe_upload_to_server(url, self.create_attachment_filename(attachment.filename),
                                                     attachment.data, attachment.mime_type)
            return self.safe_save_doc_file(file_string, attachment.filename)

    @staticmethod
    def create_attachment_filename(filename):
        _, extension = os.path.splitext(filename)
        return 'attachment' + extension

    @safe_call_and_log_if_failed
    def safe_upload_to_server(self, url, filename, data, mime_type):
        """
        Uploads data to given url and saves it with given filename and mime_type

        :return: Raw response, returned by post request
        """
        if url:
            request = requests.post(url, files={'file': (filename or 'NoName', data, mime_type)})
            response = json.loads(request.text)
            if 'file' in response:
                return response['file']
            elif 'error' in response:
                raise Exception(response['error'])

    @safe_call_and_log_if_failed
    def safe_save_doc_file(self, file_string, title):
        """
        Saves file on VK server by given string

        :param file_string: String, returned after uploading file
        :return: Saved document
        :rtype: VkDocument
        """
        if file_string:
            self.initialize_vkapi()
            responses = self.vkapi.docs.save(file=file_string, title=title)
            return VkDocument(responses[0])

    @safe_call_and_log_if_failed
    def safe_docs_get_upload_server(self):
        """
        Retrieves upload_url for storing files
        """
        self.initialize_vkapi()
        return self.vkapi.docs.getUploadServer()['upload_url']

    @staticmethod
    def wrap_mail(mail):
        return LamaBeautifier.get_random_mail_pattern().format(
            subject=mail.subject,
            sender=mail.sender,
            body=mail.body)

    def ifilter_directed_messages(self, messages):
        return ifilter(lambda m: m.body.encode('utf-8').startswith('Лама, '), self.ifilter_messages_with_body(messages))

    @staticmethod
    def ifilter_messages_with_body(messages):
        return ifilter(lambda m: m.body is not None, messages)

    @staticmethod
    def ifilter_private_messages(messages):
        return ifilter(lambda m: m.is_private, messages)

    @staticmethod
    def ifilter_dialog_messages(messages):
        return ifilter(lambda m: m.is_from_chat, messages)

    @staticmethod
    def ifilter_unread_messages(messages):
        return ifilter(lambda m: m.is_unread, messages)

    def mark_message_as_read(self, message):
        self.mark_message_as_read_by_id(message.id)

    @safe_call_and_log_if_failed(default=False)
    def safe_mark_message_as_read_and_log_if_failed(self, message):
        self.mark_message_as_read(message)
        return True

    def mark_message_as_read_by_id(self, message_ids):
        self.vkapi.messages.markAsRead(message_ids=message_ids)

    def register_plugin(self, plugin):
        self._plugins.append(plugin)
        plugin.bot = self

    def split_to_words(self, body):
        return body.encode('utf-8').translate(string.maketrans('', ''), string.punctuation).split()