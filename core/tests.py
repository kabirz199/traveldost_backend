from django.test import TestCase
from .models import Trip, Group

class TripModelTest(TestCase):

    def setUp(self):
        self.group = Group.objects.create(name="Test Group", trip_count=0)

    def test_create_trip_with_priority(self):
        trip = Trip.objects.create(
            group=self.group,
            trip_spot="Hill Station",
            destination="Munnar",
            description="A beautiful hill station.",
            price=2500.00,
            duration="3 Days",
            url="https://example.com/munnar",
            trip_priority=1,
            destination_priority=2
        )

        # Test trip string representation
        self.assertEqual(str(trip), "Hill Station---Test Group")

        # Test if priority fields are stored
        self.assertEqual(trip.trip_priority, 1)
        self.assertEqual(trip.destination_priority, 2)

        # Test if trip_count incremented
        self.group.refresh_from_db()
        self.assertEqual(self.group.trip_count, 1)

    def test_delete_trip_decrements_trip_count(self):
        trip = Trip.objects.create(
            group=self.group,
            trip_spot="Beach Side",
            destination="Goa",
            description="Sun, Sand and Sea.",
            price=3500.00,
            duration="4 Days",
            url="https://example.com/goa"
        )

        self.assertEqual(self.group.trip_count, 1)

        trip.delete()
        self.group.refresh_from_db()
        self.assertEqual(self.group.trip_count, 0)
