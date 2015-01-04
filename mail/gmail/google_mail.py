import base64
import email
from itertools import ifilter
from mail.gmail.google_attachment import GoogleAttachment
from mail.mail import Mail


__all__ = ['GoogleMail']


class GoogleMail(Mail):
    def __init__(self, response):
        self.response = response
        super(GoogleMail, self).__init__(self.retrieve_id(),
                                         self.retrieve_subject(),
                                         self.retrieve_body(),
                                         self.retrieve_sender(),
                                         self.retrieve_attachments())

    def retrieve_id(self):
        return self.response['id']

    def retrieve_subject(self):
        return self.retrieve_value_from_headers('Subject')

    def retrieve_body(self):
        text_parts = self.retrieve_text_parts(self.payload)
        plain_text_parts = filter(self.is_plain_text, text_parts)
        selected_part = (plain_text_parts or text_parts or [None])[0]
        return self.decode_body(selected_part['body']['data']) if selected_part else ''

    def retrieve_sender(self):
        return self.retrieve_value_from_headers('From')

    def retrieve_attachments(self):
        message_id = self.retrieve_id()
        return map(lambda r: GoogleAttachment(message_id, r), self.iterate_raw_attachments(self.payload))

    def retrieve_data_from_mail_headers(self, name):
        headers = self.response['payload']['headers']
        return next((h for h in headers if h['name'] == name), dict())

    def retrieve_value_from_headers(self, name, default=None):
        return self.retrieve_data_from_mail_headers(name).get('value', default)

    def retrieve_text_parts(self, payload):
        return filter(self.is_text, self.iterate_all_parts(payload))

    def iterate_raw_attachments(self, payload):
        return ifilter(self.is_attachment, self.iterate_all_parts(payload))

    @staticmethod
    def get_parts(payload):
        return payload.get('parts', [])

    @staticmethod
    def get_mime_type(payload):
        """
        Returns MimeType of payload
        :rtype : str
        """
        return payload.get('mimeType', '')

    @staticmethod
    def decode_body(body):
        """
        Decodes body from base64
        """
        msg_str = base64.urlsafe_b64decode(body.encode('utf8'))
        return email.message_from_string(msg_str).as_string().decode('utf8')

    @property
    def payload(self):
        return self.response['payload']

    def is_multipart(self, payload):
        """
        Checks if payload contains multiple parts
        :rtype : bool
        """
        return self.get_mime_type(payload).startswith('multipart')

    def is_text(self, payload):
        """
        Checks if payload contains text
        :return: bool
        """
        return self.get_mime_type(payload).startswith('text')

    @staticmethod
    def is_attachment(payload):
        """
        The payload contains attachment if it contains filename
        :param payload:
        :return:
        """
        return 'filename' in payload and payload['filename']

    def is_plain_text(self, payload):
        """
        Checks if payload contains plain text
        :rtype : bool
        """
        return self.get_mime_type(payload) == 'text/plain'

    def iterate_all_parts(self, payload):
        if self.is_multipart(payload):
            for part in self.get_parts(payload):
                for p in self.iterate_all_parts(part):
                    yield p
        else:
            yield payload