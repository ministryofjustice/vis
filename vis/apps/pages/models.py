from collections import OrderedDict

from django.db import models
from django.shortcuts import redirect
from django.utils.functional import cached_property
from django.conf.urls import url
from django.template.response import TemplateResponse

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, \
    PageChooserPanel, PublishingPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailadmin.views.home import SiteSummaryPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable

from wagtailextra.models import BaseVISPage, Page
from wagtailextra.mixins import ObjectListMixin

from modelcluster.fields import ParentalKey

from info.models import GlossaryItem, ExternalLink

from .forms import SearchForm

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


class PCCSearchPage(BaseVISPage):
    def get_template(self, request):
        if "q" in request.GET:
            return "pages/pcc_no_results.jade"
        return "pages/pcc_search_page.jade"

    def get_context(self, request):
        context = super(BaseVISPage, self).get_context(request)
        context["q"] = request.GET.get("q")
        return context

    def serve(self, request):
        q = request.GET.get("q")

        if q:
            form = SearchForm(data=request.GET)
            if form.is_valid():
                postcode = form.cleaned_data["q"]
                pcc = form.cleaned_data["pcc"]

                return redirect(u'%s%s/' % (pcc.url, postcode))
        return super(BaseVISPage, self).serve(request)


class PCCPage(RoutablePageMixin, BaseVISPage):
    content = RichTextField(blank=True)
    service_name = models.CharField(blank=True, max_length=2000)
    service_website_url = models.URLField(blank=True, max_length=2000)
    show_service_website_thumb = models.BooleanField(default=True)
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

    # subpage_urls = (
    #     url(r'(?i)(?P<postcode>(G[I1]R\s*[0O]AA)|([A-PR-UWYZ01][A-Z01]?)([0-9IO][0-9A-HJKMNPR-YIO]?)([0-9IO])([ABD-HJLNPQ-Z10]{2}))/$', pcc_view, name='pcc_postcode_view'),
    #     url(r'^$', pcc_view, name='pcc_page'),
    # )

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

    @route(r'(?i)(?P<postcode>(G[I1]R\s*[0O]AA)|([A-PR-UWYZ01][A-Z01]?)([0-9IO][0-9A-HJKMNPR-YIO]?)([0-9IO])([ABD-HJLNPQ-Z10]{2}))/$', name='pcc_postcode_view')
    @route(r'^$', name='pcc_page')
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


class ExternalPage(Page):
    """
    Adds the ability to redirect to an external URL from the home page or elsewhere.
    Combines the meta data and workflow of a page without actual content beyonsd a URL.
    """

    external_url = models.URLField(
        help_text="The external link to redirect the user to, e.g. https://www.gov.uk/.",
    )

    def __init__(self, *args, **kwargs):
        super(ExternalPage, self).__init__(*args, **kwargs)
        title = self._meta.get_field_by_name("title")[0]
        title.help_text = (
            "The name of the page in the admin page chooser and in the user's status bar on hover. "
            "Once they click the link they will be redirected to the external_url."
        )
        slug = self._meta.get_field_by_name("slug")[0]
        slug.help_text = (
            "The name of the page as it will appear in the user's status bar "
            "e.g http://domain.com/blog/[my-slug]/ when the use hovers over the link"
        )
        seo_title = self._meta.get_field_by_name("seo_title")[0]
        seo_title.help_text = (
            "Irrelevant when using external links. The page title is controled by the target page."
        )
        search_description = self._meta.get_field_by_name("search_description")[0]
        search_description.help_text = (
            "Seach does not work for external links because the content is not stored here"
        )

    def serve(self, request):
        return redirect(self.external_url, permanent=False)


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

    panels = [
        FieldPanel('title'),
        FieldPanel('content', classname="full"),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True


class PromoPanel(Panel):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        ImageChooserPanel('image'),
    ] + Panel.panels

    class Meta:
        abstract = True


class LeadPanel(Panel):
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
        SnippetChooserPanel('glossary_item')
    ]


class SimplePageLinkItems(Orderable, models.Model):
    page = ParentalKey('pages.SimplePage', related_name='link_items')
    link_item = models.ForeignKey(ExternalLink, related_name='+')

    panels = [
        SnippetChooserPanel('link_item')
    ]

# #### PAGE ADMIN


SimplePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('content', classname="full"),

    InlinePanel(SimplePage, 'link_items', label='Link items'),
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
    FieldPanel('show_service_website_thumb', classname="full"),
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

ExternalPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('external_url', classname="full"),
]

ExternalPage.promote_panels = [
    FieldPanel('slug'),
    FieldPanel('seo_title'),
    FieldPanel('show_in_menus'),
    FieldPanel('search_description'),
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
