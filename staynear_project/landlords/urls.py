from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='landlord_dashboard'),
    path('add-property/', views.add_property, name='add_property'),
]