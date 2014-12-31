# coding=utf-8
"""
This module defined class for Lama Bot
"""
from itertools import imap, ifilter
import time
import logging
import vk
from lama_beautifier import LamaBeautifier
from vk_message import VkMessage

__all__ = ['LamaBot']


class LamaBot(object):
    def __init__(self, app_id, mail_manager, chat_id=1, wait_for_before_check_mails=60, **kwargs):
        """
        Initializes Lama Bot.

        Expects login/password or access_token as named parameters

        :param mail_manager: A manager for retrieving mails
        :type mail_manager: AbstractMailManager

        :param chat_id: Chat identifier
        :type chat_id: int

        :raise ValueError: When neither login/password nor access_token was provided
        """
        self.version = '0.1 alpha'
        self.app_id = app_id

        self.access_token = None
        self.password = None
        self.login = None
        self.vkapi = None
        self.commands = {}

        self.initialize_commands()

        self.mail_manager = mail_manager
        self.wait_for_before_check_mails = wait_for_before_check_mails

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
            'post_to_dialog': self.post_message_to_dialog
        }

    def notify_about_unread_mails(self):
        for m in self.unread_mails:
            posted, exception = self.try_post_mail(m)
            if posted:
                self.mail_manager.mark_mail_as_read(m)
            else:
                logging.error(exception)

    def check_private_messages(self):
        for m in filter(lambda x: x.body is not None, self.safe_unread_private_messages):
            self.execute(m.body)
            self.mark_message_as_read(m)

    @property
    def unread_mails(self):
        self.mail_manager.reset_connection()
        return self.mail_manager.unread_mails

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
    def safe_private_messages_iter(self):
        return self.ifilter_private_messages(self.safe_messages_iter)

    @property
    def messages_iter(self):
        return imap(VkMessage, self.raw_messages)

    @property
    def safe_messages_iter(self):
        return imap(VkMessage, self.try_get_raw_messages_and_log_if_failed)

    @property
    def raw_messages(self):
        self.initialize_vkapi()
        response = self.vkapi.messages.get()
        return response.get('items', [])

    @property
    def try_get_raw_messages(self):
        """
        Safe retrieving messages.

        :returns: pair of two elements.

        (True, messages) - no error, messages are returned
        (False, exception) - error occurred, exception returned
        """
        try:
            return True, self.raw_messages
        except Exception, e:
            return False, e

    @property
    def try_get_raw_messages_and_log_if_failed(self):
        retrieved, exception_or_messages = self.try_get_raw_messages
        if not retrieved:
            logging.error(exception_or_messages)
            return []
        else:
            return exception_or_messages

    def try_post_mail(self, mail):
        return self.try_post_message(self.wrap_mail(mail))

    def post_mail(self, mail):
        self.post_message_to_dialog(self.wrap_mail(mail))

    def try_post_message(self, message):
        try:
            self.post_message_to_dialog(message)
            return True, None
        except Exception, e:
            return False, e

    def try_post_message_and_log_if_failed(self, message):
        posted, exception = self.try_post_message(message)
        if not posted:
            logging.error(exception)
        return posted

    def execute(self, s):
        command, args = self.split_to_command_and_argument(s)
        if command in self.commands:
            self.commands[command](args)
        else:
            self.command_not_found(command)

    def split_to_command_and_argument(self, command):
        values = command.split(':', 1)
        if len(values) != 2:
            values.append(None)
        return values[0], values[1]

    def post_message_to_dialog(self, message):
        self.initialize_vkapi()
        self.vkapi.messages.send(chat_id=self.chat_id, message=message)

    def post_welcome_message(self):
        self.post_message_to_dialog('The Lama is ready to work! (version {0})'.format(self.version))

    def command_not_found(self, command):
        message = u'Command `{}` not found'.format(command)
        self.try_post_message_and_log_if_failed(message)
        logging.warning(message)

    def run(self):
        self.post_welcome_message()

        while True:
            self.notify_about_unread_mails()
            self.check_private_messages()
            time.sleep(60)

    @staticmethod
    def wrap_mail(mail):
        return LamaBeautifier.get_random_mail_pattern().format(
            subject=mail.subject,
            sender=mail.sender,
            body=mail.body)

    @staticmethod
    def ifilter_private_messages(messages):
        return ifilter(lambda m: m.is_private, messages)

    @staticmethod
    def ifilter_unread_messages(messages):
        return ifilter(lambda m: m.is_unread, messages)

    def mark_message_as_read(self, message):
        self.mark_message_as_read_by_id(message.id)

    def mark_message_as_read_by_id(self, message_ids):
        self.vkapi.messages.markAsRead(message_ids=message_ids)


