from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    bathrooms = models.PositiveIntegerField(null=True, blank=True)
    size = models.PositiveIntegerField(null=True, blank=True)  # Size in square meters
    description = models.TextField(blank=True)
    amenities = models.JSONField(default=list, blank=True)  # List of amenities
    images = models.ImageField(upload_to='property_images/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'