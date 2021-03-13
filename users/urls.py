from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^api/users/register$', views.user_register),
    url(r'^api/users/verify/(?P<user_id>[a-z0-9\-]+)/', views.user_verify, name='user_verify'),
]
