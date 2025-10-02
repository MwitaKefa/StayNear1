from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Property, Tenant, RentPayment, MaintenanceRequest

@login_required
def landlord_dashboard(request):
    # Get stats for the dashboard
    total_properties = Property.objects.filter(landlord=request.user).count()
    occupied_properties = Tenant.objects.filter(property__landlord=request.user).count()
    pending_maintenance = MaintenanceRequest.objects.filter(property__landlord=request.user, status='pending').count()
    
    # Calculate monthly revenue (this would be more complex in reality)
    monthly_revenue = sum(
        tenant.rent_amount 
        for tenant in Tenant.objects.filter(property__landlord=request.user)
    )
    
    context = {
        'total_properties': total_properties,
        'occupied_properties': occupied_properties,
        'vacant_properties': total_properties - occupied_properties,
        'pending_maintenance': pending_maintenance,
        'monthly_revenue': monthly_revenue,
        'occupancy_rate': (occupied_properties / total_properties * 100) if total_properties > 0 else 0,
    }
    return render(request, 'landlords/dashboard.html', context)

@login_required
def properties_list(request):
    properties = Property.objects.filter(landlord=request.user)
    return render(request, 'landlords/properties.html', {'properties': properties})

@login_required
def add_property(request):
    if request.method == 'POST':
        # Handle property creation
        title = request.POST.get('title')
        property_type = request.POST.get('property_type')
        location = request.POST.get('location')
        rent_amount = request.POST.get('rent_amount')
        # ... process form data
        
        # Create new property
        property = Property.objects.create(
            landlord=request.user,
            title=title,
            property_type=property_type,
            location=location,
            rent_amount=rent_amount,
            # ... other fields
        )
        return redirect('landlord_dashboard')
    
    return render(request, 'landlords/add_property.html')