"""
This module provides class for representing VK Document
"""
from vk_objects import VkObject

__author__ = 'soon'


class VkDocument(VkObject):
    def __init__(self, response):
        super(VkDocument, self).__init__(response)
        self.type = 'doc'