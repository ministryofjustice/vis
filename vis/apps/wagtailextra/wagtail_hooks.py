from django.utils.html import format_html, format_html_join
from django.conf.urls import include, url
from django.conf import settings
from django.utils.html import escape
from django.core.urlresolvers import reverse

from wagtail.wagtailcore import hooks, rich_text
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.whitelist import attribute_rule, check_url

from . import urls

def whitelister_element_rules():
    return {
        'a': attribute_rule({'href': check_url, 'rel': True}),
    }
hooks.register('construct_whitelister_element_rules', whitelister_element_rules)

@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'wagtailextra/js/hallo-plugins/hallo-anchoredwagtaillink.js',
        'wagtailextra/js/hallo-plugins/hallo-externallink.js',
        'wagtailextra/js/hallo-plugins/hallo-disallowpastefromword.js',
        'wagtailextra/js/page-editor.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )

    return js_includes + format_html(
        """
        <script>
            window.chooserUrls.anchoredPageChooser = '%s';
            registerHalloPlugin('anchoredwagtaillink');
            registerHalloPlugin('externallink');
            registerHalloPlugin('disallowpastefromword');
        </script>
        """ % reverse('wagtailextra_chooser')
    )


class AnchoredPageLinkHandler(object):
    """
    PageLinkHandler will be invoked whenever we encounter an <a> element in HTML content
    with an attribute of data-linktype="page". The resulting element in the database
    representation will be:
    <a linktype="page" id="42">hello world</a>
    """
    @staticmethod
    def get_db_attributes(tag):
        """
        Given an <a> tag that we've identified as a page link embed (because it has a
        data-linktype="page" attribute), return a dict of the attributes we should
        have on the resulting <a linktype="page"> element.
        """
        return {'id': tag['data-id'], 'anchor': tag.get('data-anchor', '')}

    @staticmethod
    def expand_db_attributes(attrs, for_editor):
        try:
            page = Page.objects.get(id=attrs['id'])

            if for_editor:
                editor_attrs = 'data-linktype="page" data-id="%d" ' % page.id
            else:
                editor_attrs = ''

            url = page.url
            if 'anchor' in attrs:
                anchor = attrs['anchor']
                url += '#%s' % anchor
                editor_attrs += 'data-anchor="%s"' % anchor
            return '<a %shref="%s">' % (editor_attrs, escape(url))
        except Page.DoesNotExist:
            return "<a>"


rich_text.LINK_HANDLERS['page'] = AnchoredPageLinkHandler


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^wagtailadminextra/', include(urls)),
    ]
