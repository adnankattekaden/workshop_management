from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User,auth
from  workshope.models import Client
from workshope.serializers import ClientSerializer  
from rest_framework import status
from django.http import Http404


# Create your views here.

class CreateClientDetails(APIView):
    def get(self,request):
        client_data = Client.objects.all()
        if client_data:
            client_serialize = ClientSerializer(client_data,many=False)
        return Response({"status":"okeyy"})

    def post(self,request):
        full_name = request.data['full_name']
        mobile_number = request.data['mobile_number']
        place = request.data['place']
        zipcode = request.data['zipcode']
        Client.objects.create(name=full_name,mobile_number=mobile_number,place=place,zipcode=zipcode)
        return Response({'status':"client Created"})

class EditClientDetails(APIView):
    def get(self,request,id):
        client_details = Client.objects.get(id=id)
        if client_details:
            client_serialize = ClientSerializer(client_details,many=False)
            return Response(client_serialize.data)
        else:
            return Response({"status":"not avalible"})

    def put(self,request,id):
        client_details =  Client.objects.get(id=id)

        if client_details:
            full_name = request.data['full_name']
            mobile_number = request.data['mobile_number']
            place = request.data['place']
            zipcode = request.data['zipcode']
            client_details.name = full_name
            client_details.mobile_number = mobile_number
            client_details.place = place
            client_details.zipcode = zipcode
            client_details.save()
            return Response({"status":"edited"})
        else:
            return Response({"status":"no Post Available"})

    def delete(self,request,id):
        client_details =  Client.objects.get(id=id).delete()
        return Response({"status":"item Deleted"})



        
