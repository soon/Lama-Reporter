from lama import LamaBot

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['LamaPlugin']

class LamaPlugin(object):
    def __init__(self):
        self._bot = None

    def process_input(self, user_input, words, message):
        """
        Reacts on given user_input
        Returns
        :param user_input:
        :return:
        """
        pass

    @property
    def bot(self):
        """
        :rtype : LamaBot
        """
        return self._bot

    @bot.setter
    def bot(self, value):
        assert isinstance(value, LamaBot), 'Expected type LamaBot, got {}'.format(type(value))
        self._bot = value