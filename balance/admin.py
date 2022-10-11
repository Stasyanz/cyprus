from django.contrib import admin
from django.db.models import Sum, Count, Avg
from balance.models import Transaction, Wallet


class TransactionAdmin(admin.ModelAdmin):
    """Admin site model representation"""
    list_display = ["hash", "ledger_index", "amount", "account", "wallet", "destination_tag", "fee", ]
    search_fields = ["hash", "ledger_index", "amount", "account", "wallet", "destination_tag", "fee", ]
    list_filter = ["wallet", "account", "amount",  "fee", ]


admin.site.register(Wallet,)
admin.site.register(Transaction, TransactionAdmin)
