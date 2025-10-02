from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Property  # Assuming you will create a Property model in models.py
from django.contrib import messages

def dashboard(request):
    # Logic to retrieve properties for the landlord's dashboard
    properties = Property.objects.filter(landlord=request.user)  # Assuming a relationship with the user
    return render(request, 'landlords/dashboard.html', {'properties': properties})

def add_property(request):
    if request.method == 'POST':
        # Logic to handle property creation
        title = request.POST.get('title')
        property_type = request.POST.get('property_type')
        location = request.POST.get('location')
        rent_amount = request.POST.get('rent_amount')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        size = request.POST.get('size')
        description = request.POST.get('description')
        amenities = request.POST.getlist('amenities')
        images = request.FILES.getlist('images')

        # Create and save the property instance
        property_instance = Property(
            title=title,
            property_type=property_type,
            location=location,
            rent_amount=rent_amount,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            size=size,
            description=description,
            landlord=request.user  # Assuming a relationship with the user
        )
        property_instance.save()

        # Logic to handle images and amenities can be added here

        messages.success(request, 'Property added successfully!')
        return redirect('landlord_dashboard')  # Redirect to the dashboard after adding

    return render(request, 'landlords/add_property.html')