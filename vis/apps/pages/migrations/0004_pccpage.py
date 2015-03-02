# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import pages.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('pages', '0003_auto_20150220_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='PCCPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(pages.mixins.JadePageMixin, 'wagtailcore.page'),
        ),
    ]
