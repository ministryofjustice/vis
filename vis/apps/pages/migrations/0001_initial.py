# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import modelcluster.fields
import wagtailextra.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20150217_1638'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailextra.mixins.JadePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='HomePagePanels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(help_text=b'Panel Title', max_length=255)),
                ('content', models.TextField(help_text=b'Panel Body')),
                ('link_text', models.CharField(help_text=b'Link Text', max_length=255, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePagePromoPanels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(help_text=b'Panel Title', max_length=255)),
                ('content', models.TextField(help_text=b'Panel Body')),
                ('link_text', models.CharField(help_text=b'Link Text', max_length=255, blank=True)),
                ('icon_classname', models.CharField(help_text=b'Icon class name', max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.RichTextField()),
                ('menu_title', models.CharField(help_text=b'Menu title', max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailextra.mixins.JadePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='SimplePageGlosseryItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('glossary_item', models.ForeignKey(related_name='+', to='info.GlossaryItem')),
                ('page', modelcluster.fields.ParentalKey(related_name='glossary_items', to='pages.SimplePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='homepagepromopanels',
            name='link_page',
            field=models.ForeignKey(related_name='+', blank=True, to='pages.SimplePage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagepromopanels',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='promo_panels', to='pages.HomePage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagepanels',
            name='link_page',
            field=models.ForeignKey(related_name='+', blank=True, to='pages.SimplePage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagepanels',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='panels', to='pages.HomePage'),
            preserve_default=True,
        ),
    ]
