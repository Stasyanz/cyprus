"""Repo"""

from balance.models import Transaction, Wallet


def save_transactions_list(tx_list: list):
    """Saving to database"""
    for tx in tx_list:
        print(tx)
        wallet, created = Wallet.objects.get_or_create(address=tx['wallet'])
        if wallet:
            tx['wallet'] = wallet
            Transaction.objects.get_or_create(
                hash=tx['hash'],
                ledger_index=tx['ledger_index'],
                wallet=wallet,
                fee=tx['fee'],
                amount=tx['amount'],
                account=tx['account'],
                destination_tag=tx['destination_tag']
            )
