from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers

from balance.views import TransactionViewSet, GenerateTransactions


router = routers.DefaultRouter()
# router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)
# router.register(r'get_data/', GenerateTransactions.as_view())


urlpatterns = [
    path("admin/", admin.site.urls),
    path(r'', RedirectView.as_view(url='api/', permanent=False), name='index'),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/get_data/(?P<address>.+)/$', GenerateTransactions.as_view(), name="get_data"),
]
