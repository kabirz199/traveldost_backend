from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
import tempfile
from PIL import Image
import io
from rest_framework.test import APITestCase, APIClient


class TripViewSetTests(APITestCase):

    def setUp(self):
        self.group = Group.objects.create(name="Test Group")
        self.trip = Trip.objects.create(
            trip_spot="Test Spot",
            destination="Test Destination",
            description="Test Description",
            price=99.99,
            duration="2 days",
            group=self.group
        )
        self.client = APIClient()

    def test_create_trip_image(self):
        # Create a dummy image file
        image = Image.new('RGB', (100, 100), color='red')
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)

        uploaded_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_io.read(),
            content_type='image/jpeg'
        )

        trip_image = TripImage.objects.create(trip=self.trip, image=uploaded_file)

        self.assertEqual(trip_image.trip, self.trip)
        self.assertTrue(trip_image.image.name.startswith('trip_images/'))
        self.assertIn("test_image", trip_image.image.name)
