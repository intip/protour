# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from pacote.models import Pacote

import watson


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating ``created`` and ``modified``
    fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


watson.register(Pacote)
