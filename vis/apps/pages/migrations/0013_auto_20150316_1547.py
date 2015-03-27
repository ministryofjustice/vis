# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20150312_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pccpage',
            old_name='browsershot_url',
            new_name='service_website_url',
        ),
        migrations.AddField(
            model_name='pccpage',
            name='phoneline_cost',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pccpage',
            name='service_description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pccpage',
            name='service_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pccpage',
            name='service_opening_hours',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pccpage',
            name='service_phone_number',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
