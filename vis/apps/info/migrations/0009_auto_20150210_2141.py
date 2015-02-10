# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_auto_20150210_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryitem',
            name='slug',
            field=models.SlugField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
