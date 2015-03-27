# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_homepageleadpanels'),
    ]

    operations = [
        migrations.AddField(
            model_name='pccpage',
            name='browsershot_url',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
