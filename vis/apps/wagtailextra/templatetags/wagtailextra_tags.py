from django import template

register = template.Library()


@register.filter
def is_pcc_user(user):
    return user.groups.filter(name='PCCEditor').exists()
