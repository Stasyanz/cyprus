"""Balance Seriaizers"""

from typing import Optional

from rest_framework import serializers
from pydantic import BaseModel, Field

from balance.models import Transaction, Wallet


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    """Wallet model serializer"""
    url = serializers.HyperlinkedIdentityField(view_name='wallet-detail')
    transactions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='transaction-detail',
    )

    class Meta:
        model = Wallet
        fields = ['url', 'address', 'transactions']


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    """Transaction model serializer"""
    url = serializers.HyperlinkedIdentityField(view_name='transaction-detail')

    class Meta:
        model = Transaction
        exclude = ['fee', 'destination_tag', 'ledger_index',  'account', ]


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    """Transaction model serializer"""
    class Meta:
        model = Transaction
        exclude = []


class TransactionModel(BaseModel):
    """Transaction pydantic model"""
    account: str
    amount: int
    ledger_index: int
    wallet: str = Field(alias='destination')
    destination_tag: Optional[int]  # приходит не всегда
    hash: str
    fee: int

    class Config:
        allow_population_by_field_name = True
