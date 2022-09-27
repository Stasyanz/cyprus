"""Views module"""

from rest_framework import viewsets, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from loguru import logger

from balance.serializers import TransactionSerializer, TransactionsSerializer
from balance.models import Transaction
from balance.services import get_transactions_list, get_client
from balance.repository import save_transactions_list


class TransactionViewSet(
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    API endpoint that allows Txns to be viewed.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TransactionSerializer
        return TransactionsSerializer


class GenerateTransactions(APIView):
    """ This view make and external api call, save the result and return
        the response"""

    def get(self, request, address):  # чтобы из браузера запускать
        client = get_client()
        transaction_objects_list = get_transactions_list(address, client)
        try:
            save_transactions_list(transaction_objects_list)
        except Exception as ex:
            logger.error(f"Error during saving transactions list: {ex}")
            return Response({"status": "Bad"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"status": "Ok"}, status=status.HTTP_200_OK)
