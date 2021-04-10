from django.conf.urls import url
from financials import views

urlpatterns = [
    url(r'^api/pgfinancial/init/all', views.polygon_tickers_financial_async),
    url(r'^api/pgfinancial/percentile/all', views.polygon_tickers_financial_percentile),
    url(r'^api/pgfinancial/(?P<symbol>[\w\-]+)$', views.ticker_financial),
    url(r'^api/v2/pgfinancial/(?P<symbol>[\w\-]+)$', views.ticker_financial_async),
]
