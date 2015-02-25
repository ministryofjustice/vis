from django.db import models

from autoslug import AutoSlugField

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel


@register_snippet
class GlossaryItem(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, editable=False, max_length=255)
    description = RichTextField()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.slug

    panels = [
        FieldPanel('name', classname="full title"),
        FieldPanel('description', classname="full"),
    ]


@register_snippet
class Helpline(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=False, max_length=255)
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
