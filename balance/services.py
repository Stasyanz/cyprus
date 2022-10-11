"""Services"""
import re
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
    transaction_objects_list = []
    if account_transactions:
        for message in account_transactions:
            tx_data = message['tx']
            tx_data = dict_to_snake(tx_data)
            data = TransactionModel(**tx_data)
            transaction_objects_list.append(data.dict())
    return transaction_objects_list


def camel_to_snake_case(name: str) -> str:
    """Make snake case"""
    snake = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return snake


def dict_to_snake(camel_dict: dict) -> dict:
    """Dict keys to snake case"""
    snake_dict = {}
    for key, value in camel_dict.items():
        key = camel_to_snake_case(key)
        snake_dict[key] = value
    return snake_dict
