"""Repo"""

from balance.models import Transaction


def save_transactions_list(tx_list: list):
    """Saving to database"""
    for tx in tx_list:
        Transaction.objects.get_or_create(**tx)  # TODO: bulk_create
