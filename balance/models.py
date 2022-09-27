"""Balance models"""

from django.db import models


class Transaction(models.Model):
    """Transaction model"""
    hash = models.CharField(max_length=200, unique=True, primary_key=True)
    ledger_index = models.IntegerField()
    Amount = models.IntegerField()
    Account = models.CharField(max_length=200)
    Destination = models.CharField(max_length=200)
    DestinationTag = models.CharField(max_length=200, null=True, default=None)  # приходит не всегда
    Fee = models.IntegerField()

    def __str__(self):
        return '%s' % self.hash
