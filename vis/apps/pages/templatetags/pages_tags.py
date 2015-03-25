from django import template

from pages.models import PCCPage
from core.url2png import Url2Png

register = template.Library()


@register.assignment_tag
def get_pcc_list():
    return PCCPage.objects.live()


@register.simple_tag
def url2png(url):
    if url:
        raw = Url2Png(url)
        return raw.build_url()
    else:
        return ''
