from django.conf.urls import url
from pgfinancials import views

urlpatterns = [
    url(r'^api/pgfinancial/all$', views.func1),
    url(r'^api/pgfinancial/(?P<symbol>[\w\-]+)$', views.financial_ticker_polygon),

]
