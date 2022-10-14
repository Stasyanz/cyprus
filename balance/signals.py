""""""

from django.db.models.signals import post_save
from django.dispatch import receiver

from balance.models import Wallet
from balance.tasks import generate_transactions


@receiver(post_save, sender=Wallet)
def save_wallet_callback(sender, instance, **kwargs):
    generate_transactions.delay(instance.address)
