from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page


class JadePageMixin(object):

    def get_template(self, request, *args, **kwargs):
        template_path = super(JadePageMixin, self).get_template(request, *args, **kwargs)
        return template_path.replace('.html', '.jade')

class HomePage(JadePageMixin, Page):
    pass

class SimplePage(JadePageMixin, Page):

    content = RichTextField()

SimplePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('content', classname="full"),
    ]
