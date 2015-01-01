"""
This module defines base class for mail managers
"""
from utils import safe_call_and_log_if_failed


__all__ = ['AbstractMailManager']


class AbstractMailManager(object):
    def mark_mail_as_read(self, mail):
        self.mark_mail_as_read_by_id(mail.id)

    @safe_call_and_log_if_failed
    def safe_mark_mail_as_read_and_log_if_failed(self, mail):
        self.mark_mail_as_read(mail)

    def mark_mail_as_read_by_id(self, mail_id):
        raise NotImplementedError()

    @property
    def unread_mails(self):
        raise NotImplementedError()

    @property
    @safe_call_and_log_if_failed(default=[])
    def safe_unread_mails(self):
        return self.unread_mails