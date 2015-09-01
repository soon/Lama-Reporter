from vk_objects import VkObject

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['VkUser']


class VkUser(VkObject):
    def __init__(self, response):
        super(VkUser, self).__init__(response)
        self.first_name = response.get('first_name', '')
        self.last_name = response.get('last_name', '')

    def __repr__(self):
        return 'VkUser<{} {}>'.format(self.first_name, self.last_name)