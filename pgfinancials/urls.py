from django.conf.urls import url
from pgfinancials import views

urlpatterns = [
    url(r'^api/pgfinancial/(?P<symbol>[\w\-]+)$', views.ticker_financial),
    url(r'^api/v2/pgfinancial/(?P<symbol>[\w\-]+)$', views.ticker_financial_async),
]
