"""Balance models"""

import datetime

from django.db import models


class Transaction(models.Model):
    """Transaction model"""
    hash = models.CharField(max_length=200, unique=True, primary_key=True)
    ledger_index = models.CharField(max_length=200)
    Amount = models.CharField(max_length=200)
    Account = models.CharField(max_length=200)
    Destination = models.CharField(max_length=200)
    DestinationTag = models.CharField(max_length=200, null=True, default=None)
    Fee = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.hash
