__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class VkObject(object):
    def __init__(self, response):
        self.id = response.get('id', None)
        self.owner_id = response.get('owner_id', None)
        self.type = 'REPLACE_WITH_REAL_TYPE'

    @property
    def attachment_string(self):
        return '{type}{owner_id}_{id}'.format(type=self.type, owner_id=self.owner_id, id=self.id)