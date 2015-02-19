# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20150210_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryitem',
            name='slug',
            field=models.SlugField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
