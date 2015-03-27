# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_pccpage_show_generic_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='pccpage',
            name='trackmycrime_url',
            field=models.URLField(max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
