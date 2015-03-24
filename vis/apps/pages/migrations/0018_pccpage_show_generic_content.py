# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20150318_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='pccpage',
            name='show_generic_content',
            field=models.BooleanField(default=False, help_text=b'If ticked, it will render generic content instead.            You would still be able to preview the edited content but it             would not go live until this flag in unticked.'),
            preserve_default=True,
        ),
    ]
