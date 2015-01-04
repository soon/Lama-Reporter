from bs4 import BeautifulSoup


__all__ = ['Mail']


class Mail(object):
    def __init__(self, mail_id, subject, body, sender, attachments):
        self.id = mail_id
        self.subject = subject
        self.body = BeautifulSoup(body).get_text()
        self.sender = sender
        self.attachments = attachments

    def __repr__(self):
        return unicode(self)

    def __unicode__(self):
        return u'[{0}]\n\n{1}'.format(self.subject, self.body)