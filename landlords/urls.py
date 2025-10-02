from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.landlord_dashboard, name='landlord_dashboard'),
    path('properties/', views.properties_list, name='properties_list'),
    path('properties/add/', views.add_property, name='add_property'),
    # Add more URLs as needed
]