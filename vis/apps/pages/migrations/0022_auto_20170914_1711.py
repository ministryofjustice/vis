# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0019_externallink'),
        ('pages', '0021_externalpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePageLinkItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_item', models.ForeignKey(related_name='+', to='info.ExternalLink')),
                ('page', modelcluster.fields.ParentalKey(related_name='link_items', to='pages.SimplePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='externalpage',
            name='external_url',
            field=models.URLField(help_text=b'The external link to redirect the user to, e.g. https://www.gov.uk/.'),
            preserve_default=True,
        ),
    ]
