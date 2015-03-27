from django import template
from info.models import DynamicContent

register = template.Library()

@register.filter
def dynamic_content(slug):
    try:
        ret = DynamicContent.objects.get(slug=slug)
    except DynamicContent.DoesNotExist:
        return ''
    return ret.content
