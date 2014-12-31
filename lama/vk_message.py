"""
This module provides classes for representing VK message object
"""

__author__ = 'soon'

__all__ = ['VkMessageReadState', 'VkMessageType', 'VkMessage']


class VkMessageReadState(object):
    Unread = 0
    Read = 1


class VkMessageType(object):
    Received = 0
    Sent = 1


class VkMessage(object):
    def __init__(self, response):
        self.id = response.get('id', None)
        self.user_id = response.get('user_id', None)
        self.read_state = response.get('read_state', None)
        self.out = response.get('out', None)
        self.title = response.get('title', None)
        self.body = response.get('body', None)
        self.chat_id = response.get('chat_id', None)

    @property
    def is_unread(self):
        return self.read_state == VkMessageReadState.Unread

    @property
    def is_from_chat(self):
        return self.chat_id is not None

    @property
    def is_private(self):
        return not self.is_from_chat