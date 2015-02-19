# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_homepagepanels'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePagePromoPanels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(help_text=b'Panel Title', max_length=255)),
                ('content', models.TextField(help_text=b'Panel Body')),
                ('icon_classname', models.CharField(help_text=b'Icon class name', max_length=255)),
                ('link_page', models.ForeignKey(related_name='+', blank=True, to='core.SimplePage', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='promo_panels', to='core.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
