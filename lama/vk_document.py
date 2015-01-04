"""
This module provides class for representing VK Document
"""

__author__ = 'soon'


class VkDocument(object):
    def __init__(self, response):
        self.id = response.get('id', None)
        self.owner_id = response.get('owner_id', None)

    @property
    def attachment_string(self):
        return '{type}{owner_id}_{id}'.format(type='doc', owner_id=self.owner_id, id=self.id)