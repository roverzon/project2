from django.conf.urls import url
from open_and_close import views


urlpatterns = [
    url(r'^api/trading/(?P<symbol>[\w\-]+)$', views.open_and_close_detail),
    url(r'^api/trading_init/(?P<symbol>[\w\-]+)$', views.open_and_close_detail_init),
    url(r'^api/trading/tickers/all$', views.open_and_close_all_tickers),
    url(r'^api/trading/tickers/v3/all$', views.open_and_close_all_tickers_v3),
    url(r'^api/snapshot/tickers/all$', views.snapshot_all_tickers),
]
