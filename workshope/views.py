from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User,auth
from . models import *
from . serializers import *


# Create your views here.

class ClientDetails(APIView):
    def get(self,request):
        client_details = Client.objects.all()
        if client_details:
            client_serialize = ClientSerializer(client_details,Many=True)
            return Response(client_serialize.data)
        else:
            return Response({'status':'No Clients Right Now'})

    def post(self,request):
        full_name = request.data['full_name']
        mobile_number = request.data['mobile_number']
        place = request.data['place']
        zipcode = request.data['zipcode']
        Client.objects.create(name=full_name,mobile_number=mobile_number,place=place,zipcode=zipcode)
        return Response({'status':"client Created"})