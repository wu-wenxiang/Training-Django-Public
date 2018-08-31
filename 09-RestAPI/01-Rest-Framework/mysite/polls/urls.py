from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^time/plus/(\d{1,2})', views.hours_ahead, name='hours_ahead'),
    url(r'^time/', views.current_datetime, name='current_datetime'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]