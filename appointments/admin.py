from django.contrib import admin
from .models import Appointment

# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('email', 'body', 'read')
    list_filter = ('read')


admin.site.site_header = 'DGB adminz'
admin.site.register(Appointment)
