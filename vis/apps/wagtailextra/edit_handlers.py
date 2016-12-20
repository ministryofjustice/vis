from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from wagtail.wagtailadmin.edit_handlers import BaseFieldPanel, FieldPanel


class BaseCoreFieldPanel(BaseFieldPanel):
    field_template = "wagtailextra/edit_handlers/core_field_panel_field.html"

    def render_as_field(self, show_help_text=True):

        return mark_safe(render_to_string(self.field_template, {
            'is_core': self.instance.is_core,
            'field': self.bound_field,
            'field_type': self.field_type(),
            'show_help_text': show_help_text,
        }))


class CoreFieldPanel(object):
    def __init__(self, field_name, classname=""):
        self.field_name = field_name
        self.classname = classname

    def bind_to_model(self, model):
        base = {
            'model': model,
            'field_name': self.field_name,
            'classname': self.classname,
        }

        return type(str('_CoreFieldPanel'), (BaseCoreFieldPanel,), base)


class BaseConfigurableRichTextFieldPanel(BaseFieldPanel):
    def render_js(self):
        return mark_safe(
            "makeAndConfigureRichTextEditable(fixPrefix('%s'), %s);" % (
                self.bound_field.id_for_label, self.plugins
            )
        )


def ConfigurableRichTextFieldPanel(field_name, plugins):
    return type(str('_RichTextFieldPanel'), (BaseConfigurableRichTextFieldPanel,), {
        'field_name': field_name,
        'plugins': plugins
    })
