from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Property  
from django.contrib import messages

def landlords(request):
    # Temporarily remove login restriction for development
    # properties = Property.objects.filter(landlord=request.user)  # would require auth
    properties = Property.objects.all()  # show all properties instead
    return render(request, 'landlords/dashboard.html', {'properties': properties})

def add_property(request):
    # Temporarily remove login restriction for development
    
    if request.method == 'POST':
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

        # Create and save the property instance (landlord left blank for now)
        property_instance = Property(
            title=title,
            property_type=property_type,
            location=location,
            rent_amount=rent_amount,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            size=size,
            description=description,
            landlord=None  # No logged-in user for now
        )
        property_instance.save()

        messages.success(request, 'Property added successfully!')
        return redirect('landlords')  # go back to landlords page after adding

    return render(request, 'landlords/add_property.html')
