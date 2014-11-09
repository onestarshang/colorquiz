from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'langcolor.views.home'),
    # url(r'^langcolor/', include('langcolor.foo.urls')),
    url(r'^colorquiz/', include('colorquiz.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
