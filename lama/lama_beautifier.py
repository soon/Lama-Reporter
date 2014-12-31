# coding=utf-8
import random

__author__ = 'soon'

__all__ = ['LamaBeautifier']


class LamaBeautifier(object):
    mail_patterns = [
        u'Hey guys, Ich habe eine mail "{subject}", from [{sender}] wow:\n{body}',
        u'Wup! Received a new message with subject "{subject}" from [{sender}], wow:\n{body}',
        u'Алоха! На наш ящик упало письмо с темой "{subject}" от [{sender}], зацените:\n{body}',
        u'Such mail! Much problems! Many Plaksins "{subject}" from [{sender}], wow!\n{body}',
    ]

    @staticmethod
    def get_random_mail_pattern():
        return random.choice(LamaBeautifier.mail_patterns)