from django.conf.urls import patterns, url
from demo import views

urlpatterns = patterns(
    'demo.views',
    url(r'^demo/', 'demo'),  
    url(r'^data-energy/', 'energy'),  
    url(r'^data-voltage/', 'voltage'),
    url(r'^measurement/(?P<voltage>.+)/(?P<current>.+)/(?P<enabled>.+)/', 'measurement'),
    url(r'^demoControl/', 'demoControl'),
    
    )
