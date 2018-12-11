# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtailextra.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('pages', '0022_auto_20170914_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='PCCSearchPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('is_core', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailextra.mixins.JadePageMixin, 'wagtailcore.page'),
        ),
    ]
