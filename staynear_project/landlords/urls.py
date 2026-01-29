from django.urls import path
from . import views

urlpatterns = [
    path('lanlords/', views.landlords, name='landlord'),
    path('add-property/', views.add_property, name='add_property'),
]