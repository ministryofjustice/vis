from collections import OrderedDict

from django.db import models
from django.shortcuts import redirect
from django.utils.functional import cached_property
from django.conf.urls import url
from django.template.response import TemplateResponse

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, \
    PageChooserPanel, PublishingPanel
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
from wagtail.wagtailadmin.views.home import SiteSummaryPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable

from wagtailextra.models import BaseVISPage
from wagtailextra.mixins import ObjectListMixin

from modelcluster.fields import ParentalKey

from info.models import GlossaryItem


from .wagtail_constants import COMMON_PROMOTE_PANELS, \
    SIMPLEPAGE_PROMOTE_PANELS

# #### PAGES


class HomePage(BaseVISPage):
    pass


class SimplePage(BaseVISPage):
    content = RichTextField()
    menu_title = models.CharField(max_length=255, help_text="Menu title", blank=True)
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super(SimplePage, self).get_context(request, *args, **kwargs)
        parent = self.get_parent()
        if parent.specific_class == MultiPagePage:
            context['show_siblings'] = True
        return context

    @cached_property
    def live_siblings(self):
        return [x for x in self.get_siblings() if x.live]

    def get_prev_live_sibling(self):
        siblings = self.live_siblings
        od = OrderedDict([(x.pk,x) for x in siblings])
        index = od.keys().index(self.pk)

        if index > 0:
            return siblings[index - 1]

    def get_next_live_sibling(self):
        siblings = self.live_siblings
        od = OrderedDict([(x.pk,x) for x in siblings])
        index = od.keys().index(self.pk)

        if index + 1 < len(siblings):
            return siblings[index + 1]


class GlossaryPage(ObjectListMixin, BaseVISPage):
    object_class = GlossaryItem


class PCCPage(RoutablePageMixin, BaseVISPage):
    content = RichTextField(blank=True)
    service_name = models.CharField(blank=True, max_length=2000)
    service_website_url = models.URLField(blank=True, max_length=2000)
    service_phone_number = models.CharField(blank=True, max_length=2000)
    phoneline_cost = models.CharField(blank=True, max_length=2000)
    service_opening_hours = models.CharField(blank=True, max_length=2000)
    trackmycrime_url = models.URLField(blank=True, max_length=2000)
    pcc_slug = models.SlugField(
        help_text="Unique pcc slug, please do not change it.",
        editable=False
    )
    show_generic_content = models.BooleanField(
        default=False,
        help_text="If ticked, it will render generic content instead.\
            You would still be able to preview the edited content but it \
            would not go live until this flag in unticked."
    )

    subpage_types = []

    subpage_urls = (
        url(r'(?i)(?P<postcode>(G[I1]R\s*[0O]AA)|([A-PR-UWYZ01][A-Z01]?)([0-9IO][0-9A-HJKMNPR-YIO]?)([0-9IO])([ABD-HJLNPQ-Z10]{2}))/$', 'pcc_view', name='pcc_postcode_view'),
        url(r'^$', 'pcc_view', name='pcc_page'),
    )

    def get_context(self, request, *args, **kwargs):
        context = super(PCCPage, self).get_context(request, *args, **kwargs)
        postcode = kwargs.get('postcode', '')
        in_preview_mode = kwargs.get('in_preview_mode', False)

        if len(postcode) > 3:
            postcode = list(postcode)
            postcode.insert(-3, ' ')
            postcode = ''.join(postcode)

        context['postcode'] = postcode
        context['in_preview_mode'] = in_preview_mode
        return context

    def serve_preview(self, request, mode_name):
        view, args, kwargs = self.resolve_subpage('/')
        kwargs['in_preview_mode'] = True
        return view(request, *args, **kwargs)

    def pcc_view(self, request, *args, **kwargs):
        return TemplateResponse(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs)
        )


class PCCListPage(ObjectListMixin, BaseVISPage):
    object_class = PCCPage
    subpage_types = []

    def get_object_list_queryset(self):
        return self.object_class.objects.live()


class MultiPagePage(BaseVISPage):
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


class LeadPanel(PromoPanel):
    class Meta:
        abstract = True


class HomePagePromoPanels(Orderable, PromoPanel):
    page = ParentalKey('pages.HomePage', related_name='promo_panels')


class HomePageLeadPanels(Orderable, LeadPanel):
    page = ParentalKey('pages.HomePage', related_name='lead_panels')


class HomePagePanels(Orderable, Panel):
    page = ParentalKey('pages.HomePage', related_name='panels')


class SimplePageGlosseryItems(Orderable, models.Model):
    page = ParentalKey('pages.SimplePage', related_name='glossary_items')
    glossary_item = models.ForeignKey(GlossaryItem, related_name='+')

    panels = [
        SnippetChooserPanel('glossary_item', GlossaryItem)
    ]


# #### PAGE ADMIN


SimplePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('content', classname="full"),

    InlinePanel(SimplePage, 'glossary_items', label='Glossary items'),
]
SimplePage.promote_panels = SIMPLEPAGE_PROMOTE_PANELS


HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel(HomePage, 'lead_panels', label="Lead Panels"),
    InlinePanel(HomePage, 'panels', label="Panels"),
    InlinePanel(HomePage, 'promo_panels', label="Promo Panels"),
]
HomePage.promote_panels = COMMON_PROMOTE_PANELS


PCCPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('service_name', classname="full"),
    FieldPanel('content', classname="full"),
    FieldPanel('service_website_url', classname="full"),
    FieldPanel('service_phone_number', classname="full"),
    FieldPanel('phoneline_cost', classname="full"),
    FieldPanel('service_opening_hours', classname="full"),
    FieldPanel('trackmycrime_url', classname="full"),
]
PCCPage.promote_panels = COMMON_PROMOTE_PANELS
PCCPage.settings_panels = [
    PublishingPanel(),
    FieldPanel('show_generic_content'),
]


MultiPagePage.promote_panels = COMMON_PROMOTE_PANELS
GlossaryPage.promote_panels = COMMON_PROMOTE_PANELS
PCCListPage.promote_panels = COMMON_PROMOTE_PANELS


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
