"""Services"""

from typing import List

from xrpl.clients import JsonRpcClient
from xrpl.account import get_account_payment_transactions

from balance.serializers import TransactionModel
from rpl.settings import JSON_RPC_URL


def get_client() -> JsonRpcClient:
    """Get ripple client"""
    return JsonRpcClient(JSON_RPC_URL)


def get_transactions_list(address: str, client: JsonRpcClient) -> List[dict]:
    """Get account transactions"""
    account_transactions: list = get_account_payment_transactions(address=address, client=client)
    transaction_objects_list = [ ]
    if account_transactions:
        for message in account_transactions:
            tx_data = message["tx"]
            data = TransactionModel(**tx_data)
            transaction_objects_list.append(data.dict())
    return transaction_objects_list
