# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_auto_20150210_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpline',
            name='slug',
            field=models.SlugField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
