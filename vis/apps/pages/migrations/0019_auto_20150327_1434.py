# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from pages.models import PCCPage
from bs4 import BeautifulSoup
from django.contrib.contenttypes.models import ContentType

import json


def get_latest_revision(page):
    return page.revisions.order_by('-created_at').first()


def fix_content(content):
    soup = BeautifulSoup(content)
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href.startswith(('http', 'https', 'www')):
            link['rel'] = 'external'

    return soup.find('body').decode_contents()


def update_page(page):
    if not hasattr(page, 'content'):
        return

    page.content = fix_content(page.content)
    page.save()


def update_revision(page):
    latest_revision = get_latest_revision(page)

    if not latest_revision:
        return

    data = json.loads(latest_revision.content_json)

    if 'content' not in data:
        return

    data['content'] = fix_content(data['content'])

    latest_revision.content_json = json.dumps(data)
    latest_revision.save()


def get_specific_page(page):
    content_type = ContentType.objects.get_for_id(page.content_type_id)
    if isinstance(page, content_type.model_class()):
        # page is already the an instance of the most specific class
        return page
    else:
        return content_type.get_object_for_this_type(id=page.id)


def add_external_rel_attr(apps, schema_editor):
    Page = apps.get_model("wagtailcore", "Page")

    for page in Page.objects.all():
        page = get_specific_page(page)

        update_page(page)
        update_revision(page)

    GlossaryItem = apps.get_model("info", "GlossaryItem");

    for item in GlossaryItem.objects.all():
        item.description = fix_content(item.description)
        item.save()


def revert(apps, schema_editor):
    return


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_pccpage_show_generic_content'),
        ('info', '0016_auto_20150227_1623'),
    ]

    operations = [
        migrations.RunPython(add_external_rel_attr, reverse_code=revert),
    ]
