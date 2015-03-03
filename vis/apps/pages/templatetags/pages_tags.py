from django import template

from pages.models import PCCPage

register = template.Library()


@register.assignment_tag
def get_pcc_list():
    return PCCPage.objects.all()
