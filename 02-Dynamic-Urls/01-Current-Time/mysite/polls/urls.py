from django.conf.urls import url

from . import views

urlpatterns = [
    url('^time/', views.current_datetime, name='current_datetime'),
    url('^$', views.index, name='index'),
]