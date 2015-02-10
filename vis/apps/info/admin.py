from django.contrib import admin

from .models import GlossaryItem
from .models import Helpline


class GlossaryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    list_editable = ('name', 'slug', 'description')


class HelplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'url')
    list_editable = ('name', 'phone', 'url')


admin.site.register(GlossaryItem, GlossaryItemAdmin)
admin.site.register(Helpline, HelplineAdmin)
