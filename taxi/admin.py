from django.contrib import admin
from .models import Driver, Manufacturer, Car

admin.site.register(Manufacturer)
admin.site.register(Car)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['username', 'license_number']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Additional info', {'fields': ('license_number',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Additional info', {'fields': ('license_number',)}),
    )
    search_fields = ['model']
    list_filter = ['manufacturer__name']
