from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from balance.views import GenerateTransactions, WalletViewSet, TransactionViewSet


router = routers.DefaultRouter()
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^api/get-data/(?P<address>.+)/$', GenerateTransactions.as_view(), name="get_data"),
    path(r'', RedirectView.as_view(url='api/', permanent=False), name='index'),
    path('api/', include(router.urls)),
]
