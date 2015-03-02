# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_helpline_ordering'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='helpline',
            options={'ordering': ['ordering']},
        ),
        migrations.AlterField(
            model_name='glossaryitem',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, max_length=255, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='helpline',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, max_length=255, editable=False),
            preserve_default=True,
        ),
    ]
