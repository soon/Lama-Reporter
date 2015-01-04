import base64
from mail.attachment import Attachment

__author__ = 'soon'


class GoogleAttachment(Attachment):
    def __init__(self, message_id, response):
        self.response = response
        self.base64_encoded_data = self.body.get('data', None)
        super(GoogleAttachment, self).__init__(self.retrieve_id(), message_id, self.retrieve_data())

    def retrieve_id(self):
        return self.body.get('attachmentId', None)

    def retrieve_data(self):
        if self.base64_encoded_data is not None:
            return base64.urlsafe_b64decode(self.base64_encoded_data.encode('utf8'))
        else:
            return None

    @property
    def body(self):
        return self.response.get('body', {})

    def load(self, manager):
        response = manager.attachments_get(id=self.id, messageId=self.message_id).execute()
        self.data = response.get('data', None)