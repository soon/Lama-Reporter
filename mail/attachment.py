"""
This module provides class for representing mail attachment
"""
from utils import safe_call_and_log_if_failed

__author__ = 'soon'

__all__ = ['Attachment']


class Attachment(object):
    def __init__(self, attachment_id, message_id, data):
        self.id = attachment_id
        self.message_id = message_id
        self.data = data

    @property
    def is_loaded(self):
        return self.data is not None

    def load(self, manager):
        """
        Loads attachment using the given manager
        :param manager:
        :return:
        """
        raise NotImplementedError()

    @safe_call_and_log_if_failed
    def safe_load(self, manager):
        self.load(manager)