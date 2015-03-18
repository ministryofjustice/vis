# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtailextra.mixins
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('pages', '0004_pccpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PCCListPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(pages.models.ObjectListMixin, wagtailextra.mixins.JadePageMixin, 'wagtailcore.page'),
        ),
    ]
