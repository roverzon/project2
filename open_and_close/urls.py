from django.conf.urls import url
from open_and_close import views


urlpatterns = [
    url(r'^api/trading/(?P<symbol>[\w\-]+)$', views.open_and_close_detail),
    url(r'^api/daily/trading/(?P<symbol>[\w\-]+)$', views.ticker_open_and_close_daily),
    url(r'^api/weekly/trading/(?P<symbol>[\w\-]+)$', views.ticker_open_and_close_weekly),
    url(r'^api/trading/last/(?P<symbol>[\w\-]+)$', views.last_stock_open_and_close),
    url(r'^api/trading/tickers/v3/all$', views.open_and_close_all_tickers_v3),
    url(r'^api/snapshot/tickers/all$', views.snapshot_all_tickers),
]
