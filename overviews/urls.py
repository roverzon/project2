from django.conf.urls import url
from overviews import views


urlpatterns = [
    url(r'^api/overviews$', views.overview_list),
    url(r'^api/overviews/init$', views.overview_init),
    url(r'^api/overviews/(?P<symbol>[\w\-]+)$', views.overview_detail),
    url(r'^api/v2/overviews/(?P<symbol>[\w\-]+)$', views.alpha_vantage_company_overview),
    url(r'^api/v2/overviews/financials/(?P<symbol>[\w\-]+)$', views.alpha_vantage_company_overview_and_financials),
]
