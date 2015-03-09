from django.conf.urls import url
from .views import chooser


urlpatterns = [
    url(r'^chooser/$', chooser.chooser, name='wagtailextra_chooser'),
]
