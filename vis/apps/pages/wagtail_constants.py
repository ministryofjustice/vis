from django.utils.translation import ugettext_lazy

from wagtailextra.edit_handlers import CoreFieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    MultiFieldPanel


def build_promote_panels(items):
    return [
        MultiFieldPanel(items, ugettext_lazy('Common page configuration')),
    ]

COMMON_PROMOTE_PANELS = build_promote_panels([
        CoreFieldPanel('slug'),
        FieldPanel('seo_title'),
        FieldPanel('show_in_menus'),
        FieldPanel('search_description'),
    ]
)

SIMPLEPAGE_PROMOTE_PANELS = build_promote_panels([
        CoreFieldPanel('slug'),
        FieldPanel('seo_title'),
        FieldPanel('show_in_menus'),
        FieldPanel('menu_title'),
        FieldPanel('search_description'),
    ]
)
