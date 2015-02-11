from __future__ import absolute_import
from django.contrib import admin
from django.db import models

from django_markdown.widgets import MarkdownWidget
from rules.contrib.admin import ObjectPermissionsModelAdmin

from .models import PCC


class PCCAdmin(ObjectPermissionsModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MarkdownWidget},
    }

admin.site.register(PCC, PCCAdmin)
