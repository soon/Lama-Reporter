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
    tea = ['чай']
    please = ['пожалуйста']
    this = ['это']
    person = ['господин']
    resources_directory = 'resources'
    two_coffee_directory = 'two_coffee'
    one_tea_directory = 'one_tea_with_cookies'

    @safe_call_and_log_if_failed
    def process_input(self, user_input, words, normalized_words, message):
        if self.words_contains_any_of_all(normalized_words, self.two, self.coffee + self.tea):
            if not self.words_contains_any_of(normalized_words, self.please):
                self.bot.post_message_to_dialog(u'А где пожалуйста?', forward_messages=[message])
            elif self.words_contains_any_of_all(normalized_words, self.this, self.person):
                if len(message.fwd_messages) == 1:
                    self.bot.vkapi_messages_set_activity_in_chat()
                    photo = self.bot.safe_upload_message_photo(self.get_appropriate_image(normalized_words))
                    user = self.bot.retrieve_users_by_ids(message.first_fwd_message.user_id)[0]
                    self.bot.post_message_to_dialog(
                        u'{first_name} {last_name}, это вам от столика №{number}'.format(first_name=user.first_name,
                                                                                         last_name=user.last_name,
                                                                                         number=random.randint(1, 19)),
                        forward_messages=[message], attachments=[photo])
                else:
                    self.bot.post_message_to_dialog(u'И кому это?', forward_messages=[message])
            else:
                self.bot.vkapi_messages_set_activity_in_chat()
                photo = self.bot.safe_upload_message_photo(self.get_appropriate_image(normalized_words))
                m = self.get_appropriate_message(normalized_words)
                self.bot.post_message_to_dialog(m, forward_messages=[message], attachments=[photo])

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
            return u'Аромагия Якобс, ммм...'
        elif self.words_contains_any_of(words, self.tea):
            return u'Простите, у нас остался только один'
        else:
            return ''
