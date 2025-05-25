from django.test import TestCase
from .models import Group, Trip

class TripCountTestCase(TestCase):
    def setUp(self):
        # Create a group
        self.group = Group.objects.create(
            name="Adventure Club",
            url="https://example.com",
            about_us="We go on thrilling adventures!"
        )

    def test_trip_count_increases_on_create(self):
        # Initially trip count should be 0
        self.assertEqual(self.group.trip_count, 0)

        # Add one trip
        Trip.objects.create(
            group=self.group,
            trip_spot="Nainital",
            destination="Uttarakhand",
            description="Lake city trip",
            price=5000,
            duration="3 Days")
