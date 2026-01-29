from django.urls import path
from . import views
from staynear_project.listings import views as listing_views  # Import listings views

urlpatterns = [
    path('', views.home, name='home'),
]