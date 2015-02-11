from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django_markdown import flatpages

from django.contrib import admin
admin.autodiscover()
flatpages.register()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    url(r'^police/', include('police.urls')),
    url(r'^glossary/', include('info.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
)
