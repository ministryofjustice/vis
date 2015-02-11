from django.conf.urls import patterns, url

from .views import pcc_search, PCCDetail


urlpatterns = patterns(
    '',
    url(r'^search/$', pcc_search),
    url(r'^(?P<slug>[a-z-]+)/$', PCCDetail.as_view(), name='pcc_detail')
)
