from django.conf.urls import url
from summary import views

urlpatterns = [
    url(r'^api/summary/trade$', views.candle_line_alert),
    url(r'^api/summary/price_return$', views.ticker_price_return),
    url(r'^api/summary/price_return/percentile$', views.ticker_price_percentile),
    url(r'^api/summary/price_return/async$', views.ticker_price_return_async),
    url(r'^api/summary/ta/(?P<symbol>[\w\-]+)$$', views.technical_indicator_MACD),
]
