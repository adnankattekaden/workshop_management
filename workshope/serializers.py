from rest_framework import serializers
from workshope.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        models = Client
        fields = '__all__'

