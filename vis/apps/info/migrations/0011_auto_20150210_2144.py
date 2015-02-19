# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_helpline_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpline',
            name='slug',
            field=models.SlugField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
