from vk_objects import VkAttachableObject

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['VkPhoto']


class VkPhoto(VkAttachableObject):
    def __init__(self, response):
        super(VkPhoto, self).__init__(response)
        self.type = 'photo'