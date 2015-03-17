# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models, migrations


def update_pcc_slug(apps, schema_editor):
    PCCPage = apps.get_model("pages", "PCCPage")
    for page in PCCPage.objects.all():
        page.pcc_slug = page.slug
        page.save(update_fields=['pcc_slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20150316_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='pccpage',
            name='pcc_slug',
            field=models.SlugField(default=uuid.uuid4().get_hex(), help_text=b'Unique pcc slug, please do not change it.'),
            preserve_default=False,
        ),
        migrations.RunPython(update_pcc_slug, reverse_code=lambda *x: x),
    ]
