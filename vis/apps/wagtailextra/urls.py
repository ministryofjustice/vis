from django.conf.urls import url
from .views import chooser


urlpatterns = [
    url(r'^chooser/$', chooser.chooser, name='wagtailextra_chooser'),
    url(r'^chooser-page/(\d+)/$', chooser.chooser, name='wagtailextra_chooser_page_child'),
]
