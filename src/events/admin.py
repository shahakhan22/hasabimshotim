from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.get_fields()]

admin.site.register(Event, EventAdmin)
