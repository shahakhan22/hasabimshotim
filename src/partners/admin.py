from django.contrib import admin

from .models import Partner

# Register your models here.
class PartnerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Partner._meta.get_fields()]

admin.site.register(Partner, PartnerAdmin)
