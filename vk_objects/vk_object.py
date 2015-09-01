__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class VkObject(object):
    def __init__(self, response):
        self.id = response.get('id', None)