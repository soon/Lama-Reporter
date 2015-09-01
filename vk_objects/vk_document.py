"""
This module provides class for representing VK Document
"""
from vk_objects import VkAttachableObject

__author__ = 'soon'


class VkDocument(VkAttachableObject):
    def __init__(self, response):
        super(VkDocument, self).__init__(response)
        self.type = 'doc'