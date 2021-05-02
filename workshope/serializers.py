from rest_framework import serializers
from . models import *

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Client
        fields = '__all__'
