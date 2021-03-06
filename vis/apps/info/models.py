from django.db import models

from autoslug import AutoSlugField

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtailextra.edit_handlers import ConfigurableRichTextFieldPanel


@register_snippet
class GlossaryItem(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from='name', unique=True, editable=False, max_length=255)
    description = RichTextField()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.slug

    def get_letter(self):
        return self.name[0].lower()

    panels = [
        FieldPanel('name', classname="full title"),
        ConfigurableRichTextFieldPanel(
            'description', """{
                'hallowagtaillink': {}
            }"""
        ),
    ]

    class Meta:
        ordering = ['name']


@register_snippet
class ExternalLink(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from='name', unique=True, editable=False, max_length=255)
    url = models.URLField()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.slug

    def get_letter(self):
        return self.name[0].lower()

    panels = [
        FieldPanel('name', classname="full title"),
        FieldPanel('url', classname="full"),
    ]

    class Meta:
        ordering = ['name']


@register_snippet
class Helpline(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(
        populate_from='name', unique=True, editable=False, max_length=255)
    phone = models.CharField(max_length=18)
    ordering = models.PositiveSmallIntegerField(default=1000)
    url = models.URLField()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.name

    panels = [
        FieldPanel('name', classname="full title"),
        FieldPanel('phone', classname="full"),
        FieldPanel('ordering', classname="full"),
        FieldPanel('url', classname="full"),
    ]

    class Meta:
        ordering = ['ordering']


@register_snippet
class DynamicContent(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(
        populate_from='name', unique=True, editable=False, max_length=255)
    content = models.TextField()

    panels = [
        FieldPanel('name', classname="full title"),
        FieldPanel('content', classname="full"),
    ]

    def natural_key(self):
        return self.slug

    def __unicode__(self):
        return self.slug
