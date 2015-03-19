from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from wagtail.wagtailadmin.edit_handlers import BaseFieldPanel


class BaseCoreFieldPanel(BaseFieldPanel):
    field_template = "wagtailextra/edit_handlers/core_field_panel_field.html"

    def render_as_field(self, show_help_text=True):

        return mark_safe(render_to_string(self.field_template, {
            'is_core': self.instance.is_core,
            'field': self.bound_field,
            'field_type': self.field_type(),
            'show_help_text': show_help_text,
        }))


def CoreFieldPanel(field_name, classname=""):
    return type(str('_CoreFieldPanel'), (BaseCoreFieldPanel,), {
        'field_name': field_name,
        'classname': classname,
    })
