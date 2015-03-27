# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_auto_20150227_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=255, editable=False)),
                ('content', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
