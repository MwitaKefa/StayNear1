from django.test import TestCase
from .models import Property  # Adjust the import based on your actual model name

class PropertyModelTests(TestCase):
    def test_property_creation(self):
        property = Property.objects.create(
            title="Test Property",
            property_type="apartment",
            location="Test Location",
            rent_amount=25000,
            bedrooms=2,
            bathrooms=1,
            size=85,
            description="This is a test property."
        )
        self.assertEqual(property.title, "Test Property")
        self.assertEqual(property.property_type, "apartment")
        self.assertEqual(property.location, "Test Location")
        self.assertEqual(property.rent_amount, 25000)
        self.assertEqual(property.bedrooms, 2)
        self.assertEqual(property.bathrooms, 1)
        self.assertEqual(property.size, 85)
        self.assertEqual(property.description, "This is a test property.")

    # Add more tests as needed for your application logic.