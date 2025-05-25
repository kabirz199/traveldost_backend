from rest_framework import serializers
from .models import Group, Trip, InstagramModel,TripImage

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'

class InstagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramModel
        fields = '__all__'


class TripImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripImage
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)
    trip_image = TripImageSerializer(many=True, read_only=True)  # Related name used here

    class Meta:
        model = Trip
        fields = '__all__'

