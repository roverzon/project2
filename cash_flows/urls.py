from django.conf.urls import url
from cash_flows import views

urlpatterns = [
    url(r'^api/cashflows$', views.cash_flow_list),
    url(r'^api/cash_flow/init/all$', views.cash_flow_init_async),
    url(r'^api/v2/cashflow/annual/(?P<symbol>[\w\-]+)$', views.alpha_vantage_cash_flow_annual),
    url(r'^api/v2/cashflow/quarterly/(?P<symbol>[\w\-]+)$', views.alpha_vantage_cash_flow_quarterly),
    url(r'^api/cashflows/(?P<symbol>[\w\-]+)$', views.symbol_cash_flow_list),

]
