from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('bedsitter', 'Bedsitter'),
        ('single_room', 'Single Room'),
        ('commercial', 'Commercial'),
    ]
    
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=100)
    address = models.TextField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    size = models.IntegerField(help_text="Size in square meters")
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Tenant(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    move_in_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class RentPayment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    month = models.CharField(max_length=7)  # Format: YYYY-MM
    
    def __str__(self):
        return f"{self.tenant.name} - {self.month}"

class MaintenanceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    reported_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    
    def __str__(self):
        return self.title