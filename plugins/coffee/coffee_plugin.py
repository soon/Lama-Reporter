# coding=utf-8
import os
import random
from plugins import LamaPlugin
from utils import safe_call_and_log_if_failed

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['CoffeePlugin']


class CoffeePlugin(LamaPlugin):
    two = ['два', '2']
    coffee = ['кофе']
    tea = ['чай', 'чая', 'чаю']
    please = ['пожалуйста']
    this = ['этому']
    person = ['господину']
    resources_directory = 'resources'
    two_coffee_directory = 'two_coffee'
    one_tea_directory = 'one_tea_with_cookies'

    @safe_call_and_log_if_failed
    def process_input(self, user_input, words, message):
        lower_words = map(str.lower, words)
        if self.words_contains_any_of_all(words, self.two, self.coffee + self.tea):
            if not self.words_contains_any_of(lower_words, self.please):
                self.bot.post_message_to_dialog('А где пожалуйста?', forward_messages=[message])
            elif self.words_contains_any_of_all(lower_words, self.this, self.person):
                if len(message.fwd_messages) == 1:
                    photo = self.bot.safe_upload_message_photo(self.get_appropriate_image(words))
                    user = self.bot.retrieve_users_by_ids(message.first_fwd_message.user_id)[0]
                    self.bot.post_message_to_dialog(
                        '{first_name} {last_name}, это вам от столика №{number}'.format(first_name=user.first_name,
                                                                                        last_name=user.last_name,
                                                                                        number=random.randint(1, 19)),
                        forward_messages=[message], attachments=[photo])
                else:
                    self.bot.post_message_to_dialog('И кому это?', forward_messages=[message])
            else:
                photo = self.bot.safe_upload_message_photo(self.get_appropriate_image(words))
                m = self.get_appropriate_message(words)
                self.bot.post_message_to_dialog(m, forward_messages=[message], attachments=[photo])

    @staticmethod
    def words_contains_any_of_all(words, *required_kinds_of_words):
        return all(CoffeePlugin.words_contains_any_of(words, kind_of_words)
                   for kind_of_words in required_kinds_of_words)

    @staticmethod
    def words_contains_any_of(words, required_words):
        return any(w in words for w in required_words)

    @property
    def abspath_to_resources_directory(self):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), self.resources_directory)

    @property
    def abspath_to_coffee_directory(self):
        return os.path.join(self.abspath_to_resources_directory, self.two_coffee_directory)

    @property
    def abspath_to_tea_directory(self):
        return os.path.join(self.abspath_to_resources_directory, self.one_tea_directory)

    @staticmethod
    def abspath_to_random_file_from_directory(directory):
        filename = random.choice(os.listdir(directory))
        return os.path.join(directory, filename)

    @property
    def random_coffee_image(self):
        return self.abspath_to_random_file_from_directory(self.abspath_to_coffee_directory)

    @property
    def random_tea_image(self):
        return self.abspath_to_random_file_from_directory(self.abspath_to_tea_directory)

    def get_appropriate_image(self, words):
        if self.words_contains_any_of(words, self.coffee):
            return self.random_coffee_image
        elif self.words_contains_any_of(words, self.tea):
            return self.random_tea_image

    def get_appropriate_message(self, words):
        if self.words_contains_any_of(words, self.coffee):
            return 'Аромагия Якобс, ммм...'
        elif self.words_contains_any_of(words, self.tea):
            return 'Простите, у нас остался только один'
        else:
            return ''
