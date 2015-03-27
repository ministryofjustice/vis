# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20150316_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pccpage',
            name='service_description',
        ),
        migrations.AlterField(
            model_name='pccpage',
            name='content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
    ]
