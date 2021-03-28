from django.conf.urls import url
from stock_tas import views

urlpatterns = [
    url(r'^api/function/candle_pattern/all', views.scan_candle_pattern),
    url(r'^api/function/candle_pattern/(?P<symbol>[\w\-]+)$', views.candle_pattern),
]
