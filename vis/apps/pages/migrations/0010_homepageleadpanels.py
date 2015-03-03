# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('pages', '0009_remove_homepage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageLeadPanels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(help_text=b'Panel Title', max_length=255)),
                ('content', models.TextField(help_text=b'Panel Body')),
                ('link_text', models.CharField(help_text=b'Link Text', max_length=255, blank=True)),
                ('icon_classname', models.CharField(help_text=b'Icon class name', max_length=255)),
                ('link_page', models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='lead_panels', to='pages.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
