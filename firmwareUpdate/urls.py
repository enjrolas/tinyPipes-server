from django.conf.urls import patterns, url
from firmwareUpdate import views

urlpatterns = patterns('firmwareUpdate.views',
                       url(r'^$', 'firmware', name='firmware'),
)
