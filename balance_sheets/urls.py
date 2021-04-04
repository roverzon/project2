from django.conf.urls import url
from balance_sheets import views


urlpatterns = [
    url(r'^api/balancesheets$', views.balance_sheet_list),
    url(r'^api/balancesheets/init/all$', views.balance_sheet_init_async),
    url(r'^api/balancesheets/(?P<symbol>[\w\-]+)$', views.symbol_balance_sheet_list),
    url(r'^api/v2/balancesheets/annual/(?P<symbol>[\w\-]+)$', views.alpha_vantage_balance_sheet_annual),
    url(r'^api/v2/balancesheets/quarterly/(?P<symbol>[\w\-]+)$', views.alpha_vantage_balance_sheet_quarterly),
]
