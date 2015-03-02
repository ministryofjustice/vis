# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20150227_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simplepage',
            name='ordering',
        ),
    ]
