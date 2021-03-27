from django.conf.urls import url
from stock_tas import views

urlpatterns = [
    url(r'^api/function/cross_star/all', views.scan_ticker_cross_star),
    url(r'^api/v2/function/cross_star/all', views.scan_ticker_cross_star_async),
    url(r'^api/function/cross_star/(?P<symbol>[\w\-]+)$', views.scanner_cross_star),
]
