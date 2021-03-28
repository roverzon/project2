from django.conf.urls import url
from stock_tas import views

urlpatterns = [
    url(r'^api/function/cross_star/all', views.scan_tickers_inverted_hammer),
    url(r'^api/function/black_line/all', views.scan_ticker_black_line),
    url(r'^api/v2/function/cross_star/all', views.scan_tickers_inverted_hammer_async),
    url(r'^api/function/cross_star/(?P<symbol>[\w\-]+)$', views.find_ticker_inverted_hammer),
]
