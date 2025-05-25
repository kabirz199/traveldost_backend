from rest_framework import viewsets
from .models import Group, Trip, InstagramModel
from .serializers import GroupSerializer, TripSerializer, InstagramSerializer,TripImage,TripImageSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class InstagramViewSet(viewsets.ModelViewSet):
    queryset = InstagramModel.objects.all()
    serializer_class = InstagramSerializer

class TripImageViewSet(viewsets.ModelViewSet):
    queryset = TripImage.objects.all()
    serializer_class = TripImageSerializer