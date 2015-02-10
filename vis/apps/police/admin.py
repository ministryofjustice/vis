from django.contrib import admin
from .models import PCC


class PCCAdmin(admin.ModelAdmin):
    pass

admin.site.register(PCC, PCCAdmin)
