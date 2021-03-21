from django.conf.urls import url
from tickers import views


urlpatterns = [
    url(r'^api/tickers/pg/vX/all$', views.polygon_all_tickers),
    url(r'^api/tickers/pg/vX/v2/all$', views.polygon_all_tickers_v2),
]
