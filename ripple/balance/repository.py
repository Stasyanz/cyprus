"""Repo"""

from balance.models import Transaction


def save_transactions_list(tx_list: list):
    """Saving to database"""
    for tx in tx_list:
        new_tx, created = Transaction.objects.get_or_create(**tx)

