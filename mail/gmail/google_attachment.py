import base64
from mail.attachment import Attachment
from utils import safe_call_and_log_if_failed

__author__ = 'soon'


class GoogleAttachment(Attachment):
    def __init__(self, message_id, response):
        self.response = response
        self.base64_encoded_data = self.body.get('data', None)
        super(GoogleAttachment, self).__init__(self.retrieve_id(),
                                               message_id,
                                               self.retrieve_filename(),
                                               self.retrieve_data(),
                                               self.retrieve_mime_type())

    def retrieve_id(self):
        return self.body.get('attachmentId', None)

    def retrieve_data(self):
        return self.safe_decode_data(self.base64_encoded_data)

    @safe_call_and_log_if_failed
    def safe_decode_data(self, data):
        """
        Decodes data using base64 algorithm

        :param data:
        :return: Decoded data
        """
        if data is not None:
            return base64.urlsafe_b64decode(data.encode('utf8'))
        else:
            return None

    def retrieve_filename(self):
        return self.response.get('filename', None)

    def retrieve_mime_type(self):
        return self.response.get('mimeType', None)

    @property
    def body(self):
        return self.response.get('body', {})

    def load(self, manager):
        if not self.is_loaded:
            response = manager.attachments_get(id=self.id, messageId=self.message_id).execute()
            self.data = self.safe_decode_data(response.get('data', None))
