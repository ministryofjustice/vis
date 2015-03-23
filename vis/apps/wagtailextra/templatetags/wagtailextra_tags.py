from django import template

register = template.Library()

# Local cache of filters, avoid hitting the DB
filters = {}


@register.filter
def is_pcc_user(user):
    return user.groups.filter(name='PCCEditor').exists()
