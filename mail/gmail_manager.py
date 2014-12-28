"""
This module defines class for Google Mail Manager
"""
import httplib2

from apiclient.discovery import build

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

from mail.abstract_mail_manager import AbstractMailManager


__all__ = ['GMailManager']


class GMailManager(AbstractMailManager):

    def __init__(self, client_secret_json_path):
        super(GMailManager, self).__init__()

        self.oauth_scope = 'https://www.googleapis.com/auth/gmail.readonly'
        self.client_secret_file = client_secret_json_path
        self.http = self.create_http()

        self.credentials = self.retrieve_credentials()
        self.authorize_http_using_credentials()

        self.gmail_service = self.create_gmail_service()

    def retrieve_credentials(self):
        storage = Storage('gmail.storage')

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

    @property
    def unread_mails(self):
        return self.gmail_service.users().messages().list(userId='me', labelIds='UNREAD').execute()
