from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Fibonacci(models.Model):
    number = models.TextField(_('Number'))
    value = models.TextField(_('Fibonacci Value'))

    def __unicode__(self):
        return self.number
