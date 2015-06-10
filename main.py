#!/usr/bin/python2
import json
import logging
from logging.handlers import SMTPHandler
import sys

from mail import GMailManager
from lama import LamaBot
from plugins.bad_advice import BadAdvicePlugin
from plugins.bash_im import BashImPlugin
from plugins.coffee import CoffeePlugin
from plugins.good_night import GoodNightPlugin
from plugins.hello import HelloPlugin
from plugins.weather.weather_plugin import WeatherPlugin


def print_welcome():
    print 'Welcome to the Lam-o-Matic, biatch'
    print r'''
 |                              _ \                       |
 |      _` | __ `__ \   _` |   |   | _ \ __ \   _ \   __| __|  _ \  __|
 |     (   | |   |   | (   |   __ <  __/ |   | (   | |    |    __/ |
_____|\__,_|_|  _|  _|\__,_|  _| \_\___| .__/ \___/ _|   \__|\___|_|
                                        _|
         _ \ _ | _ |
\ \   / |   |  |   |
 \ \ /  |   |  |   |
  \_/  \___/_)_|_)_|

'''


def print_ready():
    print 'All systems go!'


def create_log_formatter():
    return logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M')


def create_file_log_handler(log_filename):
    handler = logging.FileHandler(log_filename, mode='w')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(create_log_formatter())
    return handler


def create_console_log_handler():
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(create_log_formatter())
    return handler


def create_smtp_log_handler(mail_host, mail_port, from_address, to_addresses, email_subject,
                            username, password, use_tls):
    secure = () if use_tls else None
    handler = SMTPHandler((mail_host, mail_port), from_address, to_addresses, email_subject,
                          credentials=(username, password), secure=secure)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(create_log_formatter())
    return handler


def add_logger_handlers(logger, *handlers):
    for handler in handlers:
        logger.addHandler(handler)


def initialize_logging(settings):
    """
    Initializes logging according to given settings
    :param settings:
    :type settings: LamaSettings
    :return:
    """
    add_logger_handlers(logging.getLogger(''),
                        create_file_log_handler(settings.log_filename),
                        create_console_log_handler(),
                        create_smtp_log_handler(settings.log_email_host_name,
                                                settings.log_email_host_port,
                                                settings.log_email_host_username,
                                                settings.log_email_admins,
                                                settings.log_email_subject,
                                                settings.log_email_host_username,
                                                settings.log_email_host_password,
                                                settings.log_email_use_tls))


class LamaSettings(object):
    def __init__(self):
        self.gmail_client_secret_json = None
        self.gmail_storage = None
        self.vk_login = None
        self.vk_password = None
        self.vk_access_token = None
        self.vk_app_id = None
        self.vk_main_chat = None
        self.vk_mail_chat = None
        self.vk_update_in_seconds = None
        self.vk_admins = None
        self.log_filename = None
        self.log_email_admins = None
        self.log_filename = None
        self.log_email_host_name = None
        self.log_email_host_port = None
        self.log_email_host_username = None
        self.log_email_host_password = None
        self.log_email_subject = None

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        settings = LamaSettings()
        settings.load_vk(data['vk'])
        settings.load_mail(data['mail'])
        settings.load_log(data['log'])
        return settings

    def load_vk(self, vk):
        self.load_vk_credentials(vk['credentials'])
        self.load_vk_chats(vk['chats'])
        self.load_vk_update_in_seconds(vk['update_in_seconds'])
        self.load_vk_admins(vk['admins'])

    def load_mail(self, mail):
        self.gmail_client_secret_json = mail['gmail_client_secret_json']
        self.gmail_storage = mail['gmail_storage']

    def load_log(self, log):
        self.load_log_filename(log['filename'])
        self.load_log_email(log['email'])

    def load_vk_credentials(self, credentials):
        self.vk_login = credentials.get('login', None)
        self.vk_password = credentials.get('password', None)
        self.vk_app_id = credentials['app_id']
        self.vk_access_token = credentials.get('access_token', None)

    def load_vk_chats(self, chats):
        self.vk_main_chat = chats['main']
        self.vk_mail_chat = chats['mails']

    def load_vk_update_in_seconds(self, update_in_seconds):
        self.vk_update_in_seconds = update_in_seconds

    def load_vk_admins(self, admins):
        self.vk_admins = admins

    def load_log_filename(self, filename):
        self.log_filename = filename

    def load_log_email(self, email):
        self.load_log_email_admins(email['admins'])
        self.load_log_email_use_tls(email.get('use_tls', False))
        self.load_log_email_host(email['host'])
        self.load_log_email_subject(email['subject'])

    def load_log_email_admins(self, admins):
        self.log_email_admins = admins

    def load_log_email_use_tls(self, use_tls):
        self.log_email_use_tls = use_tls

    def load_log_email_host(self, host):
        self.log_email_host_name = host['name']
        self.log_email_host_port = host['port']
        self.log_email_host_username = host['username']
        self.log_email_host_password = host['password']

    def load_log_email_subject(self, subject):
        self.log_email_subject = subject


def main(argv):
    settings_file = 'settings.json'
    settings = LamaSettings.from_json(open(settings_file).read())

    initialize_logging(settings)
    print_welcome()

    manager = GMailManager(settings.gmail_client_secret_json, storage_path=settings.gmail_storage)
    bot = LamaBot(settings.vk_app_id, manager, access_token=settings.vk_access_token,
                  chat_id=settings.vk_main_chat, login=settings.vk_login, password=settings.vk_password,
                  number_of_seconds_for_the_rest=settings.vk_update_in_seconds,
                  chat_id_for_mails=settings.vk_mail_chat, admins=settings.vk_admins)

    weather = WeatherPlugin('Perm,ru')
    bot.register_plugin(weather)
    bot.register_plugin(CoffeePlugin())
    bot.register_plugin(BashImPlugin())
    bot.register_plugin(BadAdvicePlugin())
    bot.register_plugin(GoodNightPlugin())
    bot.register_plugin(HelloPlugin())

    print_ready()

    post_welcome_message_to_dialog = '--no_welcome_message' not in argv

    try:
        bot.run(post_welcome_message_to_dialog)
    except (KeyboardInterrupt, SystemExit):
        print '\nBye!'
        bot.stop_running()
        bot.post_message_to_admins('Bye, bye, bye, my darling')
    except Exception:
        bot.stop_running()
        bot.post_message_to_admins('Something went wrong... See you later!')
        raise

if __name__ == '__main__':
    main(sys.argv)