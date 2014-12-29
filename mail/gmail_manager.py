"""
This module defines class for Google Mail Manager
"""
import base64
import httplib2

# noinspection PyUnresolvedReferences
from apiclient.discovery import build

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

from abstract_mail_manager import AbstractMailManager
from mail import Mail
import email

__all__ = ['GMailManager']


class GMailManager(AbstractMailManager):

    def __init__(self, client_secret_json_path, storage_path='gmail.storage'):
        super(GMailManager, self).__init__()

        self.http = None
        self.credentials = None
        self.gmail_service = None
        self.storage_path = storage_path

        self.oauth_scope = 'https://www.googleapis.com/auth/gmail.modify'
        self.client_secret_file = client_secret_json_path

        self.reset_connection()

    def reset_connection(self):
        self.http = self.create_http()

        self.credentials = self.retrieve_credentials()
        self.authorize_http_using_credentials()

        self.gmail_service = self.create_gmail_service()

    def retrieve_credentials(self):
        storage = Storage(self.storage_path)

        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = run(self.create_oauth_flow(), storage, http=self.http)

        return credentials

    def authorize_http_using_credentials(self):
        self.http = self.credentials.authorize(self.http)

    def create_oauth_flow(self):
        return flow_from_clientsecrets(self.client_secret_file, scope=self.oauth_scope)

    @staticmethod
    def create_http():
        return httplib2.Http()

    def create_gmail_service(self):
        return build('gmail', 'v1', http=self.http)

    def extract_body_from_mail(self, mail_response):
        data = mail_response['payload']['body'].get('data', '')
        print data

        if data:
            return self.decode_body(data)
        else:
            return mail_response['snippet']

    @staticmethod
    def decode_body(body):
        msg_str = base64.urlsafe_b64decode(body.encode('utf8'))
        return email.message_from_string(msg_str).as_string().decode('utf8')

    def get_mail_by_id(self, mail_id):
        response = self.messages_get(id=mail_id).execute()

        subject = self.retrieve_data_from_mail_headers(response, 'Subject').get('value', None)
        body = self.extract_body_from_mail(response)

        return Mail(mail_id, subject, body)

    def mark_mail_as_read_by_id(self, mail_id):
        self.messages_modify(id=mail_id, body={"removeLabelIds": ["UNREAD"]}).execute()

    def messages_get(self, **kwargs):
        return self.messages.get(userId='me', **kwargs)

    def messages_list(self, **kwargs):
        return self.messages.list(userId='me', **kwargs)

    def messages_modify(self, **kwargs):
        return self.messages.modify(userId='me', **kwargs)

    @staticmethod
    def retrieve_data_from_mail_headers(mail, name):
        headers = mail['payload']['headers']
        return next((h for h in headers if h['name'] == name), dict())

    @property
    def messages(self):
        return self.gmail_service.users().messages()

    @property
    def unread_mails(self):
        ids = self.messages_list(labelIds='UNREAD').execute().get('messages', [])
        return map(lambda d: self.get_mail_by_id(d['id']), ids)
