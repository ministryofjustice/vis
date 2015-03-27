# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_homepage_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='content',
        ),
    ]
