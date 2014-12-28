"""
This module defines base class for mail managers
"""


__all__ = ['AbstractMailManager']


class AbstractMailManager(object):
    def mark_mail_as_read(self, mail):
        self.mark_mail_as_read_by_id(mail.id)

    def mark_mail_as_read_by_id(self, id):
        raise NotImplementedError()

    @property
    def unread_mails(self):
        raise NotImplementedError()