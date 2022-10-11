"""Balance models"""

from django.db import models


class Wallet(models.Model):
    address = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return f'{self.address}'


class Transaction(models.Model):
    """Transaction model"""
    hash = models.CharField(max_length=200, primary_key=True)
    ledger_index = models.IntegerField()
    amount = models.IntegerField()
    account = models.CharField(max_length=200)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    destination_tag = models.CharField(max_length=200, null=True, default=None)  # приходит не всегда
    fee = models.IntegerField()

    def __str__(self):
        return f'{self.hash}'
