# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcc',
            name='slug',
            field=models.SlugField(unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
