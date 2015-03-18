# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20150317_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossarypage',
            name='is_core',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='is_core',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='multipagepage',
            name='is_core',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pcclistpage',
            name='is_core',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pccpage',
            name='is_core',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simplepage',
            name='is_core',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
    ]
