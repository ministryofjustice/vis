# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_homepagepromopanels'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagepanels',
            name='link_text',
            field=models.CharField(help_text=b'Link Text', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagepromopanels',
            name='link_text',
            field=models.CharField(help_text=b'Link Text', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
