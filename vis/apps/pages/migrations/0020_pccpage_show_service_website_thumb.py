# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_pccpage_trackmycrime_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pccpage',
            name='show_service_website_thumb',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
