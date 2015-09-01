# coding=utf-8
from plugins import LamaPlugin
from utils import safe_call_and_log_if_failed

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['GoodNightPlugin']


class GoodNightPlugin(LamaPlugin):
    good_normalized = ['добрый']
    night_normalized = ['ночь']
    to_all = ['всем']

    @safe_call_and_log_if_failed
    def process_input(self, user_input, words, normalized_words, message):
        if self.words_contains_any_of_all(normalized_words, self.good_normalized, self.night_normalized):
            if self.words_contains_any_of(words, self.to_all):
                self.bot.post_message_to_dialog(self.good_night_message_to_all)
            else:
                self.bot.post_message_to_dialog(self.good_night_message, forward_messages=[message])

    @property
    def good_night_message_to_all(self):
        return u'Всем чмоки в этом чатике!'

    @property
    def good_night_message(self):
        return u'Сладких снов, зайка'