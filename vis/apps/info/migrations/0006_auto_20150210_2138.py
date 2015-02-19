# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20150210_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossaryitem',
            name='slug',
            field=models.SlugField(default=b'', max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='glossaryitem',
            name='name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
