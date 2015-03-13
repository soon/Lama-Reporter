# coding=utf-8
from plugins import LamaPlugin
from utils import safe_call_and_log_if_failed

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['HelloPlugin']


class HelloPlugin(LamaPlugin):
    hello_normalized = ['привет', 'приветос', 'приветище', 'здравствовать']
    good_normalized = ['добрый']
    day_normalized = ['день', 'утро', 'вечер']

    @safe_call_and_log_if_failed
    def process_input(self, user_input, words, normalized_words, message):
        if (self.words_contains_any_of(normalized_words, self.hello_normalized) or
            self.words_contains_any_of_all(normalized_words, self.good_normalized, self.day_normalized)):
            self.bot.post_message_to_dialog(self.hello, forward_messages=[message])

    @property
    def hello(self):
        return 'Привет'