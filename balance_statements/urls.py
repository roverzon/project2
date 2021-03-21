from django.conf.urls import url
from balance_statements import views


urlpatterns = [
    url(r'^api/balancesheets$', views.balancesheet_list),
    url(r'^api/balancesheets/all$', views.balancesheet_init_async),
    url(r'^api/balancesheets/(?P<symbol>[\w\-]+)$', views.symbol_balancesheet_list),
    url(r'^api/v2/balancesheets/annual/(?P<symbol>[\w\-]+)$', views.alpha_vantage_balancesheet_annual),
    url(r'^api/v2/balancesheets/quarterly/(?P<symbol>[\w\-]+)$', views.alpha_vantage_balancesheet_quarterly),
]
