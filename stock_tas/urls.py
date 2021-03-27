from django.conf.urls import url
from stock_tas import views

urlpatterns = [
    url(r'^api/function/cross_star/(?P<symbol>[\w\-]+)$', views.scanner_cross_star),
]
