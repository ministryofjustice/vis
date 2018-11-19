from django import template
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from bs4 import BeautifulSoup, Tag

register = template.Library()


@register.filter
def is_pcc_user(user):
    return user.groups.filter(name='PCCEditor').exists()

@register.filter
def heading_ids(value):
    """
    Picks out the headings of a html string and assigns an ID
    to each one so that they can be linked to using an anchor link
    """
    soup = BeautifulSoup(value, 'html5lib')
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    for heading in headings:
        heading['id'] = slugify(heading.getText())

    soup.html.unwrap()
    soup.head.unwrap()
    soup.body.unwrap()
    return mark_safe(soup.prettify())
