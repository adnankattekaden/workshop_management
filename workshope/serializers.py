from rest_framework import serializers
from workshope.models import Client,Vehicle,VehicleType,JobCard,SparesInformation

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = VehicleType
        fields = '__all__'


class JobCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCard
        fields = '__all__'

class SparesInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparesInformation
        fields = '__all__'

        