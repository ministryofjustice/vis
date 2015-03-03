from django.db import models
from django.shortcuts import redirect

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, \
    PageChooserPanel, MultiFieldPanel
from wagtail.wagtailadmin.views.home import SiteSummaryPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from django.utils.translation import ugettext_lazy

from modelcluster.fields import ParentalKey

from info.models import GlossaryItem

from .mixins import JadePageMixin


# #### PAGES

class HomePage(JadePageMixin, Page):
    pass


class SimplePage(JadePageMixin, Page):
    content = RichTextField()
    menu_title = models.CharField(max_length=255, help_text="Menu title", blank=True)
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super(SimplePage, self).get_context(request, *args, **kwargs)
        parent = self.get_parent()
        if parent.specific_class == MultiPagePage:
            context['show_siblings'] = True
        return context


class ObjectListMixin(object):
    object_class = None
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super(ObjectListMixin, self).get_context(
            request, *args, **kwargs
        )

        context['object_list'] = self.object_class.objects.all()
        return context


class GlossaryPage(ObjectListMixin, JadePageMixin, Page):
    object_class = GlossaryItem


class PCCPage(JadePageMixin, Page):
    content = RichTextField()
    subpage_types = []


class PCCListPage(ObjectListMixin, JadePageMixin, Page):
    object_class = PCCPage
    subpage_types = []


class MultiPagePage(JadePageMixin, Page):
    menu_title = models.CharField(max_length=255, help_text="Menu title", blank=True)
    subpage_types = ['pages.SimplePage']

    def serve(self, request, *args, **kwargs):
        children = self.get_descendants()
        if len(children):
            return redirect(children[0].url)
        return super(MultiPagePage, self).serve(request, *args, **kwargs)

# #### PAGE COMPONENTS


class Panel(models.Model):
    title = models.CharField(max_length=255, help_text="Panel Title")
    content = models.TextField(help_text="Panel Body")
    link_page = models.ForeignKey(
        'wagtailcore.page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_text = models.CharField(max_length=255, help_text="Link Text", blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('content', classname="full"),
        PageChooserPanel('link_page'),
        FieldPanel('link_text'),
    ]

    class Meta:
        abstract = True


class PromoPanel(Panel):
    icon_classname = models.CharField(max_length=255, help_text="Icon class name")

    panels = [
        FieldPanel('icon_classname'),
    ] + Panel.panels

    class Meta:
        abstract = True


class HomePagePromoPanels(Orderable, PromoPanel):
    page = ParentalKey('pages.HomePage', related_name='promo_panels')


class HomePagePanels(Orderable, Panel):
    page = ParentalKey('pages.HomePage', related_name='panels')


class SimplePageGlosseryItems(Orderable, models.Model):
    page = ParentalKey('pages.SimplePage', related_name='glossary_items')
    glossary_item = models.ForeignKey(GlossaryItem, related_name='+')

    panels = [
        SnippetChooserPanel('glossary_item', GlossaryItem)
    ]


# #### PAGE ADMIN

COMMON_PROMOTE_PANELS = [
    MultiFieldPanel([
        FieldPanel('slug'),
        FieldPanel('seo_title'),
        FieldPanel('show_in_menus'),
        FieldPanel('menu_title'),
        FieldPanel('search_description'),
    ], ugettext_lazy('Common page configuration')),
]


SimplePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('content', classname="full"),

    InlinePanel(SimplePage, 'glossary_items', label='Glossary items'),
]


SimplePage.promote_panels = COMMON_PROMOTE_PANELS


HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel(HomePage, 'promo_panels', label="Promo Panels"),
    InlinePanel(HomePage, 'panels', label="Panels"),
]

PCCPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('content', classname="full")
]


MultiPagePage.promote_panels = COMMON_PROMOTE_PANELS

# HOOKS

from wagtail.wagtailcore import hooks


@hooks.register('after_edit_page')
def do_after_page_create(request, page):
    is_submitting = bool(request.POST.get('action-submit'))
    if is_submitting and isinstance(page, PCCPage):
        page.get_latest_revision().publish()
    return None


@hooks.register('construct_homepage_panels')
def construct_homepage_panels(request, panels):
    for index, panel in enumerate(panels):
        if isinstance(panel, SiteSummaryPanel):
            del panels[index]
