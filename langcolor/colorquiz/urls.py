
from django.conf.urls import patterns, include, url

urlpatterns = patterns('colorquiz.views',
    url(r'^$', 'index'),
    url(r'^submit/$', 'submit_answer'),
)
