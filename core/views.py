from rest_framework import viewsets
from .models import Group, Trip, InstagramModel
from .serializers import GroupSerializer, TripSerializer, InstagramSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class InstagramViewSet(viewsets.ModelViewSet):
    queryset = InstagramModel.objects.all()
    serializer_class = InstagramSerializer
