from django.conf.urls import url
from summary import views

urlpatterns = [
    url(r'^api/summary/trade$', views.candle_line_alert),
]
