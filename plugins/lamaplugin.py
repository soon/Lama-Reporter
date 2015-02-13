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

    @staticmethod
    def words_contains_any_of_all(words, *required_kinds_of_words):
        """
        Checks if given words contains any required word from all of given kinds of required words
        :param words:
        :param required_kinds_of_words:
        :return:
        """
        return all(LamaPlugin.words_contains_any_of(words, kind_of_words)
                   for kind_of_words in required_kinds_of_words)

    @staticmethod
    def words_contains_any_of(words, required_words):
        """
        Checks if given words contains any of given required words
        :param words:
        :param required_words:
        :return:
        """
        return any(w in words for w in required_words)

    @staticmethod
    def lower_words(words):
        """
        Converts given words to lowercase
        :param words:
        :return:
        """
        return map(str.lower, words)

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