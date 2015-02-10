# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20150210_2116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NationalHelpline',
            new_name='Helpline',
        ),
    ]
