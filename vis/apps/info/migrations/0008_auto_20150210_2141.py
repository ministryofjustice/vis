# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20150210_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryitem',
            name='slug',
            field=models.SlugField(max_length=255),
            preserve_default=True,
        ),
    ]
