from django.conf.urls import url
from cash_flows import views

urlpatterns = [
    url(r'^api/cashflows$', views.cashflow_list),
    url(r'^api/cash_flow/init/all$', views.cashflow_init_annual_async),
    url(r'^api/v2/cashflow/annual/(?P<symbol>[\w\-]+)$', views.alpha_vantage_cashflow_annual),
    url(r'^api/v2/cashflow/quarterly/(?P<symbol>[\w\-]+)$', views.alpha_vantage_cashflow_quarterly),
    url(r'^api/cashflows/(?P<symbol>[\w\-]+)$', views.symbol_cashflow_list),

]
