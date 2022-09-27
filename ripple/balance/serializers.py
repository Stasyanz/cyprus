"""Balance Seriaizers"""

from typing import Optional

from rest_framework import serializers
from pydantic import BaseModel

from balance.models import Transaction


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    """Transaction model serializer"""
    class Meta:
        model = Transaction
        exclude = ["Fee", "DestinationTag", "ledger_index"]


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    """Transaction model serializer"""
    class Meta:
        model = Transaction
        exclude = []


class TransactionModel(BaseModel):
    """Transaction pydantic model"""
    Account: str
    Amount: int
    ledger_index: int
    Destination: str
    DestinationTag: Optional[int]
    hash: str
    Fee: int
