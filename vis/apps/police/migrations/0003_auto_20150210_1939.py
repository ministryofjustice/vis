# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0002_auto_20150210_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pcc',
            options={'verbose_name': 'PCC', 'verbose_name_plural': 'PCCs'},
        ),
    ]
