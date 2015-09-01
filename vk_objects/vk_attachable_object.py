from vk_objects import VkObject

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['VkAttachableObject']


class VkAttachableObject(VkObject):
    def __init__(self, response):
        super(VkAttachableObject, self).__init__(response)
        self.owner_id = response.get('owner_id', None)
        self.type = 'REPLACE_WITH_REAL_TYPE'

    @property
    def attachment_string(self):
        return '{type}{owner_id}_{id}'.format(type=self.type, owner_id=self.owner_id, id=self.id)