# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_auto_20150210_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryitem',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
