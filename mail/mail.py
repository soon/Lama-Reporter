from bs4 import BeautifulSoup

class Mail(object):
    def __init__(self, id, subject, body):
        self.id = id
        self.subject = subject
        self.body = BeautifulSoup(body).get_text()

    def __repr__(self):
        return unicode(self)

    def __unicode__(self):
        return u'[{0}]\n\n{1}'.format(self.subject, self.body)