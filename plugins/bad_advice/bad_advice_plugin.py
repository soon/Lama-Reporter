# coding=utf-8
from plugins import LamaPlugin
from plugins.bad_advice import BadAdviceFactory
from utils import safe_call_and_log_if_failed

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['BadAdvicePlugin']


class BadAdvicePlugin(LamaPlugin):
    advice = ['совет', 'посоветуй']

    @safe_call_and_log_if_failed
    def process_input(self, user_input, words, message):
        lower_words = self.lower_words(words)
        if self.words_contains_any_of(lower_words, self.advice):
            self.bot.post_message_to_dialog(BadAdviceFactory.get_bad_advice(), forward_messages=[message])
