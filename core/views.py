from rest_framework import viewsets,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Group, Trip, InstagramModel
from .serializers import GroupSerializer, TripSerializer, InstagramSerializer,TripImage,TripImageSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['trip_spot', 'destination']

class InstagramViewSet(viewsets.ModelViewSet):
    queryset = InstagramModel.objects.all()
    serializer_class = InstagramSerializer

class TripImageViewSet(viewsets.ModelViewSet):
    queryset = TripImage.objects.all()
    serializer_class = TripImageSerializer

class DestinationInfoView(APIView):
    def get(self, request):
        trips = Trip.objects.all()
        destination_data = {}

        for trip in trips:
            dest = trip.destination
            if dest not in destination_data:
                # Count total trips for this destination
                trip_count = Trip.objects.filter(destination=dest).count()
                destination_data[dest] = {
                    'trip_count': trip_count,
                    'trips': []
                }
            destination_data[dest]['trips'].append(TripSerializer(trip).data)

        return Response(destination_data)