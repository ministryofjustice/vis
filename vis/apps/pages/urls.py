from django.conf.urls import patterns, url

from .views import pcc_search


urlpatterns = patterns(
    '',
    url(r'^police/search/$', pcc_search),
)
