#!/usr/bin/python2

from mail import GMailManager
from lama import LamaBot
from time import sleep

try:
    from settings import *
except ImportError:
    raise ImportError('You should place your settings into settings.py module',
                      ['VK_LOGIN', 'VK_PASSWORD', 'VK_APP_ID', 'VK_CHAT_ID'])


def main():
    manager = GMailManager('/home/soon/client_secret.json')
    bot = LamaBot(VK_APP_ID, manager, chat_id=VK_CHAT_ID, login=VK_LOGIN, password=VK_PASSWORD)

    while True:
        bot.notify_about_unread_mails()
        sleep(60)


if __name__ == '__main__':
    main()