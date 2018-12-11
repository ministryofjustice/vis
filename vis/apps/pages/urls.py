from django.conf.urls import patterns, url

from .views import pcc_search


urlpatterns = patterns(
    '',
    url(r'^find-local-support/$', pcc_search),
)
