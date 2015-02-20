# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_auto_20150217_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryitem',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
            preserve_default=True,
        ),
    ]
