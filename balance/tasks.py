"""Celery tasks"""

from loguru import logger

from balance.celery import app
from balance.services import get_client, get_transactions_list
from balance.repository import save_transactions_list


@app.task
def generate_transactions(address):
    client = get_client()
    transaction_objects_list = get_transactions_list(address, client)
    try:
        save_transactions_list(transaction_objects_list)
    except Exception as ex:
        logger.error(f"Error during saving transactions list: {ex}")
    return {'status': 'Ok'}
