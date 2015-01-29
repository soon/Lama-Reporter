from vk_objects.vk_object import VkObject

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['VkPhoto']


class VkPhoto(VkObject):
    def __init__(self, response):
        super(VkPhoto, self).__init__(response)
        self.type = 'photo'