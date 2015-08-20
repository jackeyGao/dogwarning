from django.contrib import admin

# Register your models here.
from webmanager.models import BeepSound
from webmanager.models import SayText

class BeepSoundAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SayTextAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(BeepSound, BeepSoundAdmin)
admin.site.register(SayText, SayTextAdmin)
