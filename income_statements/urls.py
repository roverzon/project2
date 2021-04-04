from django.conf.urls import url
from income_statements import views


urlpatterns = [
    url(r'^api/incomes$', views.income_list),
    url(r'^api/income_statement/init/all$', views.income_statement_init_annual_async),
    url(r'^api/incomes/(?P<symbol>[\w\-]+)$', views.symbol_income_list),
    url(r'^api/incomes/(?P<symbol>[\w\-]+)/(?P<fyear>[0-9]+)$', views.symbol_income_detail),
    url(r'^api/v2/income_statement/annual/(?P<symbol>[\w\-]+)$', views.alpha_vantage_income_statement_annual),
    url(r'^api/v2/income_statement/quarterly/(?P<symbol>[\w\-]+)$', views.alpha_vantage_income_statement_quarterly),
]
