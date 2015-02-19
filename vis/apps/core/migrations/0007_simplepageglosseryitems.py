# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20150217_1638'),
        ('core', '0006_auto_20150217_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePageGlosseryItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('glossary_item', models.ForeignKey(related_name='+', to='info.GlossaryItem')),
                ('page', modelcluster.fields.ParentalKey(related_name='glossary_items', to='core.SimplePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
