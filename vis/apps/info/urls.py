from django.conf.urls import patterns, url

from .views import GlossaryItemList


urlpatterns = patterns(
    '',
    url(r'^$', GlossaryItemList.as_view(template_name='info/glossaryitem_list.jade')),
)
