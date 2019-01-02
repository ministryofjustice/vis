# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_auto_20181217_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepagepromopanels',
            old_name='panel_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='homepageleadpanels',
            name='icon_classname',
        ),
        migrations.RemoveField(
            model_name='homepageleadpanels',
            name='link_text',
        ),
        migrations.RemoveField(
            model_name='homepageleadpanels',
            name='panel_image',
        ),
        migrations.RemoveField(
            model_name='homepagepanels',
            name='link_text',
        ),
        migrations.RemoveField(
            model_name='homepagepromopanels',
            name='icon_classname',
        ),
        migrations.RemoveField(
            model_name='homepagepromopanels',
            name='link_text',
        ),
    ]
