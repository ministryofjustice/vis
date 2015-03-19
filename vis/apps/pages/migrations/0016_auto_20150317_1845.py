# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_pccpage_pcc_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pccpage',
            name='pcc_slug',
            field=models.SlugField(help_text=b'Unique pcc slug, please do not change it.', editable=False),
            preserve_default=True,
        ),
    ]
