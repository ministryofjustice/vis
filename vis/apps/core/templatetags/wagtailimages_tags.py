from django import template

register = template.Library()

# Local cache of filters, avoid hitting the DB
filters = {}


@register.tag(name="image")
def image():
    pass
