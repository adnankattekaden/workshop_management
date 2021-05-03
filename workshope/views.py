from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User,auth
from  workshope.models import Client,Vehicle,VehicleType,JobCard,VehicleRemarks,SparesInformation
from workshope.serializers import ClientSerializer,VehicleSerializer,VehicleTypeSerializer,JobCardSerializer,SparesInformationSerializer
from rest_framework import status
from django.http import Http404
import uuid


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

class CreateVehicleDetaills(APIView):
    def get(self,request):
        vehicle_details = Vehicle.objects.all()
        if vehicle_details:
            vehicle_serialize = VehicleSerializer(vehicle_details,many=True)
            return Response(vehicle_serialize.data)
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

class EditVehicleDetaills(APIView):

    def get(self,request,id):
        vehicle_details = Vehicle.objects.get(id=id)
        if vehicle_details:
            vehicle_serialize = VehicleSerializer(vehicle_details,many=False)
            return Response(vehicle_serialize.data)
        else:
            return Response({"status":"no details available"})

    
    def put(self,request,id):
        vehicle_details = Vehicle.objects.get(id=id)
        vehicle_type_id = vehicle_details.vehicle_type
        if vehicle_details:
            vehicle_name = request.data['vehicle_name']
            vehicle_number = request.data['vehicle_number']
            vehicle_type = request.data['vehicle_type']
            blueprint_image = request.FILES['blueprint_image']

            vehicle_details.vehicle_name = vehicle_name
            vehicle_details.vehicle_number = vehicle_number
            vehicle_type_id.name = vehicle_type
            vehicle_type_id.blueprint_image = blueprint_image
            vehicle_details.save()
            vehicle_type_id.save()
            return Response({"status":"updated"})
        else:
            return Response({"status":"not available"})


    def delete(self,request,id):
        Vehicle.objects.get(id=id).delete()
        return Response({'status':"deleted"})

class CreateJobCard(APIView):
    def get(self,request):
        job_card_details = JobCard.objects.all()
        if job_card_details:
            job_card_serializer = JobCardSerializer(job_card_details,many=True)
            return Response(job_card_serializer.data)
        else:
            return Response({'status':"no jobcards Right Now"})

    def post(self,request):
        vehicle_id = request.data['vehicle_id']
        job_type = request.data['job_type']
        x_coordinates = float(request.data['x_coordinates'])
        y_coordinates = float(request.data['y_coordinates'])
        notes = request.data['notes']

        remarks = VehicleRemarks.objects.create(x_coordinates=x_coordinates,y_coordinates=y_coordinates,notes=notes)
        remarks_id = remarks
        myuuid = uuid.uuid4().hex[:8]
        tracking_id = 'track'+str(myuuid)
        estimate_amount = request.data['estimate_amount']
        job_status = request.data['job_status']

        vehicle = Vehicle.objects.get(id=vehicle_id)
        jobcard = JobCard.objects.create(vehicle=vehicle,job_card_types=job_type,tracking_id=tracking_id,estimate_amount=estimate_amount,job_status=job_status)
        jobcard.remarks.add(remarks_id)
        return Response({"status":"wowow"})

class SparesInformationView(APIView):
    def get(self,request,id):
        jobcard = JobCard.objects.get(id=id)
        spares_info = jobcard.spares_realted_info.all()
        if spares_info:
            spares_info_serializer = SparesInformationSerializer(spares_info,many=True)
            return Response(spares_info_serializer.data)
        else:
            return Response({"status":"no spares righnow"})

    def post(self,request,id):
        jobcard = JobCard.objects.get(id=id)
        spares_name = request.data['spares_name']
        description = request.data['description']
        amount = request.data['amount']
        spares_info = SparesInformation.objects.create(name=spares_name,description=description,amount=amount)
        jobcard.spares_realted_info.add(spares_info)
        return Response({'status':'woow'})
