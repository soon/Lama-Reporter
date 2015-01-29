#!/usr/bin/python2
import logging
import sys

from mail import GMailManager
from lama import LamaBot
from plugins.weather.weather_plugin import WeatherPlugin

try:
    # noinspection PyUnresolvedReferences
    from settings import (VK_LOGIN,
                          VK_PASSWORD,
                          VK_APP_ID,
                          VK_CHAT_ID,
                          GMAIL_CLIENT_SECRET_JSON,
                          GMAIL_STORAGE,
                          LOG_FILENAME)
except ImportError:
    raise ImportError('You should place your settings into settings.py module',
                      ['VK_LOGIN',
                       'VK_PASSWORD',
                       'VK_APP_ID',
                       'VK_CHAT_ID',
                       'GMAIL_CLIENT_SECRET_JSON',
                       'GMAIL_STORAGE',
                       'LOG_FILENAME'])


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


def create_file_log_handler():
    handler = logging.FileHandler(LOG_FILENAME, mode='w')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(create_log_formatter())
    return handler


def create_console_log_handler():
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(create_log_formatter())
    return handler


def add_logger_handlers(logger, *handlers):
    for handler in handlers:
        logger.addHandler(handler)


def initialize_logging():
    add_logger_handlers(logging.getLogger(''), create_file_log_handler(), create_console_log_handler())


def main(argv):
    initialize_logging()
    print_welcome()

    manager = GMailManager(GMAIL_CLIENT_SECRET_JSON, storage_path=GMAIL_STORAGE)
    bot = LamaBot(VK_APP_ID, manager, chat_id=VK_CHAT_ID, login=VK_LOGIN, password=VK_PASSWORD,
                  number_of_seconds_for_the_rest=10)

    weather = WeatherPlugin('Perm,ru')
    bot.register_plugin(weather)

    print_ready()

    post_welcome_message_to_dialog = '--no_welcome_message' not in argv

    try:
        bot.run(post_welcome_message_to_dialog)
    except (KeyboardInterrupt, SystemExit):
        print '\nBye!'
        bot.safe_post_message_and_log_if_failed('Bye, bye, bye, my darling')
    except Exception:
        bot.safe_post_message_and_log_if_failed('Something went wrong... See you later!')
        raise


if __name__ == '__main__':
    main(sys.argv)