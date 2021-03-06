from django import template

from wagtail.wagtailcore.models import Site, Page

from pages.models import PCCPage, HomePage

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings

import string

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('templatetags/core/top_menu.jade', takes_context=True)
def top_menu(context, parent, calling_page=None):
    request = context['request']
    menuitems = Page.objects.live().in_menu().not_type(PCCPage).not_type(HomePage)
    for menuitem in menuitems:
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)

    # assumes menu is only called with parent=site_root and is live + ignores `in_menu` field on homepage
    home_page = parent
    home_page.show_dropdown = False
    home_page.active = (
        # must match urls exactly as all URLs will start with homepage URL
        (calling_page.url == home_page.url) if calling_page else False
    )
    # append the home page (site_root) to the start of the menuitems
    # menuitems is actually a queryset so we need to force it into a list
    menuitems = [home_page] + list(menuitems)

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': request,
    }


@register.assignment_tag
def get_base_url():
    try:
        _id, root_path, root_url = Site.get_site_root_paths()[0]
        return root_url
    except IndexError:
        pass
    return None


@register.filter
def is_pcc_page(page):
    return isinstance(page.specific, PCCPage)


# Template tag alternative to static to append
# .min suffix in production
@register.simple_tag
def staticmin(name):
    parts = name.split('.')
    if not settings.DEBUG:
        parts.insert(-1, 'min')
    return static('.'.join(parts))


@register.filter
def fill_alphabet_blanks(groups):
    groups = groups[:]
    group_keys = [x['grouper'] for x in groups]

    for key in string.ascii_lowercase:
        if not key in group_keys:
            groups.append({
                'grouper': key,
                'list': []
            })

    groups.sort(key=lambda x: x['grouper'])

    return groups
