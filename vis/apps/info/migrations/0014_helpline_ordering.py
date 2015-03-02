# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20150217_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpline',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=1000),
            preserve_default=True,
        ),
    ]
