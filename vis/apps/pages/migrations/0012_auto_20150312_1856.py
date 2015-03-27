# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_pccpage_browsershot_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pccpage',
            name='browsershot_url',
            field=models.URLField(max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
