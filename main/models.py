from django.db import models
from django.utils.translation import ugettext_lazy as _
from mailng.admin.models import Mailbox

class ARmessage(models.Model):
    mbox = models.ForeignKey(Mailbox)
    subject = models.CharField(_('subject'), max_length=255)
    content = models.TextField(_('content'))
    enabled = models.BooleanField(_('enabled'))

class ARhistoric(models.Model):
    armessage = models.ForeignKey(ARmessage)
    last_sent = models.DateTimeField(auto_now=True)
    sender = models.TextField()
