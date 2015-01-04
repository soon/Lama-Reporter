"""
This module provides class for representing mail attachment
"""
from utils import safe_call_and_log_if_failed

__author__ = 'soon'

__all__ = ['Attachment']


class Attachment(object):
    def __init__(self, attachment_id, message_id, filename, data, mime_type):
        self.id = attachment_id
        self.message_id = message_id
        self.filename = filename
        self.data = data
        self.mime_type = mime_type

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