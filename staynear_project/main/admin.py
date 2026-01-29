from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "property_type", "location", "rent_amount", "bedrooms", "bathrooms")
    search_fields = ("title", "location", "property_type")
    list_filter = ("property_type", "location")
