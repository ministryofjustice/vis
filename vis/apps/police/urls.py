from django.conf.urls import patterns, url

from .views import pcc_search, PCCDetail


urlpatterns = patterns(
    '',
    url(r'^search/$', pcc_search),
    url(r'^(?P<slug>[a-z-]+)/$', PCCDetail.as_view(template_name='police/pcc_detail.jade'), name='pcc_detail')
)
