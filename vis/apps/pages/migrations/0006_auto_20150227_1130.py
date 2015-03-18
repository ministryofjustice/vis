# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtailextra.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('pages', '0005_pcclistpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiPagePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('menu_title', models.CharField(help_text=b'Menu title', max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailextra.mixins.JadePageMixin, 'wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=1000, help_text=b'Order'),
            preserve_default=True,
        ),
    ]
