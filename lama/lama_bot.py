# coding=utf-8
"""
This module defined class for Lama Bot
"""
import time
import logging
import vk

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

    def notify_about_unread_mails(self):
        for m in self.unread_mails:
            posted, exception = self.try_post_mail(m)
            if posted:
                self.mail_manager.mark_mail_as_read(m)
            else:
                logging.error(exception)

    @property
    def unread_mails(self):
        self.mail_manager.reset_connection()
        return self.mail_manager.unread_mails

    def try_post_mail(self, mail):
        return self.try_post_message(self.wrap_mail(mail))

    def post_mail(self, mail):
        self.post_message(self.wrap_mail(mail))

    def try_post_message(self, message):
        try:
            self.post_message(message)
            return True, None
        except Exception, e:
            return False, e

    def post_message(self, message):
        self.initialize_vkapi()
        self.vkapi.messages.send(chat_id=self.chat_id, message=message)

    def post_welcome_message(self):
        self.post_message('The Lama is ready to work! (version {0})'.format(self.version))

    def run(self):
        self.post_welcome_message()

        while True:
            self.notify_about_unread_mails()
            time.sleep(60)

    @staticmethod
    def wrap_mail(mail):
        return u'Hey guys, Ich habe eine mail "{0}", wow:\n{1}'.format(mail.subject, mail.body)
