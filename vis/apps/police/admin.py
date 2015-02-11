from __future__ import absolute_import
from django.contrib import admin

from rules.contrib.admin import ObjectPermissionsModelAdmin

from .models import PCC


class PCCAdmin(ObjectPermissionsModelAdmin):
    pass

admin.site.register(PCC, PCCAdmin)
