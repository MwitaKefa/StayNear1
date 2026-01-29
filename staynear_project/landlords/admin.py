from django.contrib import admin
from .models import Property  # Assuming you will define a Property model in models.py

admin.site.register(Property)  # Register the Property model with the admin site