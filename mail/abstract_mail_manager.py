"""
This module defines base class for mail managers
"""


__all__ = ['AbstractMailManager']


class AbstractMailManager(object):
    @property
    def unread_mails(self):
        raise NotImplementedError()