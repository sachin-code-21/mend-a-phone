from django.conf.urls import url

from . import views

app_name = 'map'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^request/$', views.customerRequest, name='Request'),
]