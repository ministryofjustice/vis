# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_auto_20150225_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glossaryitem',
            options={'ordering': ['name']},
        ),
    ]
