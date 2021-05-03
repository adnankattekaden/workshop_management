from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User,auth
from  workshope.models import Client,Vehicle,VehicleType
from workshope.serializers import ClientSerializer,CarSerializer,VehicleTypeSerializer
from rest_framework import status
from django.http import Http404


# Create your views here.

class CreateClientDetails(APIView):
    def get(self,request):
        client_data = Client.objects.all()

        if client_data:
            client_serialize = ClientSerializer(client_data,many=True)
            return Response(client_serialize.data)
        else:
            return Response({"status":"no datas"})

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

class CreateCarDetaills(APIView):
    def get(self,request):
        car_details = Vehicle.objects.all()
        if car_details:
            car_serialize = CarSerializer(car_details,many=True)
            return Response(car_serialize.data)
        else:
            return Response({"status":"no vehicle details"})

    def post(self,request):
        client_id = request.data['client_id']
        vehicle_name = request.data['vehicle_name']
        vehicle_number = request.data['vehicle_number']
        vehicle_type = request.data['vehicle_type']
        blueprint_image = request.FILES['blueprint_image']
        vehicle_type_id = VehicleType.objects.create(name=vehicle_type,blueprint_image=blueprint_image)
        client = Client.objects.get(id=client_id)
        Vehicle.objects.create(client=client,vehicle_name=vehicle_name,vehicle_type=vehicle_type_id)
        return Response({'status':"createdd"})
        