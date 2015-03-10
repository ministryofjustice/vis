import os
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.contrib.wagtailsitemaps.views import sitemap

from pages.views import Handler500, Handler404
from zendesk.views import ZendeskView

admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', TemplateView.as_view(template_name='homepage.jade')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt')),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^zendesk/$', ZendeskView.as_view(), name='zendesk'),
    url(r'', include('pages.urls')),
    url(r'', include(wagtail_urls)),
    url('^sitemap\.xml$', sitemap),
    )

# error handlers
handler500 = Handler500.as_error_view()
handler404 = Handler404.as_error_view()


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
