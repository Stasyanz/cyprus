from django.contrib import admin
from django.db.models import Sum, Count, Avg
from balance.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    """Admin site model representation"""
    list_display = ["hash", "ledger_index", "Amount", "Account", "Destination", "DestinationTag", "Fee", ]
    search_fields = ["hash", "ledger_index", "Amount", "Account", "Destination", "DestinationTag", "Fee", ]
    list_filter = ["Destination", "Account", "Amount",  "Fee", ]


admin.site.register(Transaction, TransactionAdmin)
