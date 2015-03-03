# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_dynamiccontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamiccontent',
            name='content',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
