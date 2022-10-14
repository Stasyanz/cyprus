"""Views module"""

from rest_framework import viewsets

from balance.serializers import WalletSerializer, TransactionSerializer, TransactionsSerializer
from balance.models import Transaction, Wallet


class WalletViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Wallets to be viewed.
    """
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Txns to be viewed.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TransactionSerializer
        return TransactionsSerializer
