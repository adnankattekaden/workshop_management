from rest_framework import serializers
from workshope.models import Client,Vehicle,VehicleType

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = VehicleType
        fields = '__all__'