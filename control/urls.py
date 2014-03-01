from django.conf.urls import patterns, url
from control import views

urlpatterns = patterns(
    'control.views',
    url(r'^$', 'home', name="home"),
    url(r'^sprinklers/', 'sprinklers', name='sprinklers'),
    url(r'^accounts/', 'accounts', name='accounts'),
    url(r'^logs/', 'logs', name='logs'),
    url(r'^command/', 'command', name='command'),
)
