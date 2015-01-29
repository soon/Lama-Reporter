# coding=utf-8
import os
from plugins import LamaPlugin
from utils import safe_call_and_log_if_failed

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['CoffeePlugin']


class CoffeePlugin(LamaPlugin):
    two = ['два', '2']
    coffee = ['кофе']
    please = ['пожалуйста']

    @safe_call_and_log_if_failed
    def process_input(self, user_input, words, message):
        lower_words = map(str.lower, words)
        if self.words_contains_any_of(lower_words, self.two) and self.words_contains_any_of(lower_words, self.coffee):
            if self.words_contains_any_of(lower_words, self.please):
                photo = self.bot.safe_upload_message_photo(self.get_image_path)
                self.bot.post_message_to_dialog('', forward_messages=[message], attachments=[photo])
            else:
                self.bot.post_message_to_dialog('А где пожалуйста?', forward_messages=[message])

    @staticmethod
    def words_contains_any_of(words, required_words):
        return any(w in words for w in required_words)

    @property
    def get_image_path(self):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'two_coffee.jpg')
