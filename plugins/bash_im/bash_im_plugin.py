# coding=utf-8
from itertools import imap

from bs4 import BeautifulSoup
import requests

from plugins import LamaPlugin
from utils import safe_call_and_log_if_failed


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class BashIm(object):
    def __init__(self, text, rating):
        self._text = None
        self._rating = None

        self.text = text
        self.rating = rating

    @staticmethod
    def parse_quote(text):
        soup = BeautifulSoup(text)
        return BashIm.parse_quote_from_soup(soup)

    @staticmethod
    def parse_quote_from_soup(soup):
        try:
            text = '\n'.join(soup.find(class_='text').stripped_strings)
            rating = int(soup.find(class_='rating').text)
            return BashIm(text, rating)
        except:
            return None

    @staticmethod
    def random_quotes():
        r = requests.post('http://bash.im/random')
        return filter(None, imap(BashIm.parse_quote_from_soup, BeautifulSoup(r.text).select('.quote')[:-1]))

    @staticmethod
    def best_random_quote():
        return max(BashIm.random_quotes(), key=lambda q: q.rating)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value


class BashImPlugin(LamaPlugin):
    quote = ['цитату', 'цитатку', 'процитируй', 'цитируй']
    bash_im = ['баш', 'баша']

    @safe_call_and_log_if_failed
    def process_input(self, user_input, words, message):
        lower_words = self.lower_words(words)
        if self.words_contains_any_of_all(lower_words, self.quote, self.bash_im):
            quote = BashIm.best_random_quote()
            self.bot.post_message_to_dialog(quote.text, forward_messages=[message])