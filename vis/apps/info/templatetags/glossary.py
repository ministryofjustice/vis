from django import template

from info.models import GlossaryItem

register = template.Library()


@register.inclusion_tag('templatetags/glossary/box.jade')
def glossary_box(num_items=3):
    items = GlossaryItem.objects.order_by('?')
    try:
        items = items[:num_items]
    except IndexError:
        items = items[:GlossaryItem.objects.count()]

    return {'items': items}
