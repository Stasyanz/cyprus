from django.apps import AppConfig


class BalanceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "balance"

    def ready(self):
        from balance import signals
