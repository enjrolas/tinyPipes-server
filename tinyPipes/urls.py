from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('sprinkler.urls')),
                       url(r'^', include('control.urls')),
                       url(r'^', include('demo.urls')),
                       url(r'^firmware/', include('firmwareUpdate.urls')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
