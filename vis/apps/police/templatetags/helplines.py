from django import template

from info.models import Helpline

register = template.Library()


@register.inclusion_tag('templatetags/helpline/box.jade')
def helpline_box(num_items=3):
    items = Helpline.objects.order_by('?')
    try:
        items = items[:num_items]
    except IndexError:
        items = items[:Helpline.objects.count()]

    return {'items': items}
