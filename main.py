#!/usr/bin/python2

from mail import GMailManager
from lama import LamaBot

try:
    from settings import *
except ImportError:
    raise ImportError('You should place your settings into settings.py module',
                      ['VK_LOGIN',
                       'VK_PASSWORD',
                       'VK_APP_ID',
                       'VK_CHAT_ID',
                       'GMAIL_CLIENT_SECRET_JSON',
                       'GMAIL_STORAGE'])


def print_welcome():
    print 'Welcome to the Lam-o-Matic, biatch'
    print r'''
 |                              _ \                       |
 |      _` | __ `__ \   _` |   |   | _ \ __ \   _ \   __| __|  _ \  __|
 |     (   | |   |   | (   |   __ <  __/ |   | (   | |    |    __/ |
_____|\__,_|_|  _|  _|\__,_|  _| \_\___| .__/ \___/ _|   \__|\___|_|
                                        _|
         _ \ _ |         |       |
\ \   / |   |  |    _` | | __ \  __ \   _` |
 \ \ /  |   |  |   (   | | |   | | | | (   |
  \_/  \___/_)_|  \__,_|_| .__/ _| |_|\__,_|
                          _|
'''


def print_ready():
    print 'All systems go!'


def main():
    print_welcome()

    manager = GMailManager(GMAIL_CLIENT_SECRET_JSON, storage_path=GMAIL_STORAGE)
    bot = LamaBot(VK_APP_ID, manager, chat_id=VK_CHAT_ID, login=VK_LOGIN, password=VK_PASSWORD)

    print_ready()

    try:
        bot.run()
    except (KeyboardInterrupt, SystemExit):
        print '\nBye!'
        bot.try_post_message_and_log_if_failed('Bye, bye, bye, my darling')
    except Exception:
        bot.try_post_message('Something went wrong... See you later!')
        raise

if __name__ == '__main__':
    main()