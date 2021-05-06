from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User,auth
from  workshope.models import Client,Vehicle,VehicleType,JobCard,VehicleRemarks,SparesInformation,Tickets,UserDetails
from workshope.serializers import ClientSerializer,VehicleSerializer,VehicleTypeSerializer,JobCardSerializer,SparesInformationSerializer,TicketsSerializer
from rest_framework import status
from django.http import Http404
import uuid
from rest_framework.permissions import IsAuthenticated
from workshope.permissions import check_permissionz

# Create your views here.


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = UserDetails.objects.get(user=request.user)
        permissions = check_permissionz(user)
        print(permissions,'ooo')
        if permissions['acces_granted'] == True:
            # print('admin')
            pass
        else:
            # print('staff')
            pass
        content = {'message': 'Hello, World!'}
        return Response(content)

class AdminLoginView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        auth.logout(request)
        return Response({"status":"logouted"})

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request, user)
            return Response({"status":"logined"})
        else:
            return Response({"status":"not logined"})

class CreateClientDetails(APIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)
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

class AutoFetchNumber(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        mobile_number = request.query_params['mobile_number']
        client_data = Client.objects.filter(mobile_number=mobile_number)
        if client_data:
            client_data_serializer = ClientSerializer(client_data,many=True)
            return Response(client_data_serializer.data)
        else:
            return Response({"status":"nope"})

class CreateVehicleDetaills(APIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)

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

class AutoFetchVehicle(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        client_id = request.query_params['client_id']
        client = Client.objects.get(id=client_id)
        vehicles = Vehicle.objects.filter(client=client)
        if vehicles:
            vehicle_serializer = VehicleSerializer(vehicles,many=True)
            return Response(vehicle_serializer.data)
        else:
            return Response({"status":"no_vehicles"})

class CreateJobCard(APIView):
    permission_classes = (IsAuthenticated,)

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

class EditJobCard(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,id):
        job_card_details = JobCard.objects.get(id=id)
        if job_card_details:
            job_card_serializer = JobCardSerializer(job_card_details,many=False)
            return Response(job_card_serializer.data)
        else:
            return Response({"status":"no jobs items right now"})

    def put(self,request,id):
        job_card_details = JobCard.objects.get(id=id)
        if job_card_details:
            payment_status = request.data['payment_status']
            job_status = request.data['job_status']
            job_card_details.job_status = job_status
            job_card_details.payment_status = payment_status
            job_card_details.save()
            return Response({'status':'updated'})
        else:
            return Response({'status':'no job right now'})

class SparesInformationView(APIView):
    permission_classes = (IsAuthenticated,)

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

class TrackingView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,tracking_id):
        tracking_view = JobCard.objects.get(tracking_id=tracking_id)
        if tracking_view:
            job_card_details = JobCardSerializer(tracking_view,many=False)
            return Response(job_card_details.data)
        else:
            return Response({"status":"no items avialable"})

class ListingJobs(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,status):
        jobs_data = JobCard.objects.filter(job_status=status)
        if jobs_data:
            jobs_data_serializer = JobCardSerializer(jobs_data,many=True)
            return Response(jobs_data_serializer.data)
        else:
            return Response({"status":"no jobs avialable"})

#admin only
class SalesReportView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user = UserDetails.objects.get(user=request.user)
        permissions = check_permissionz(user)
        if permissions['acces_granted'] == True:
            from_date = request.query_params['from_date']
            to_date = request.query_params['to_date']
            sales_report = JobCard.objects.filter(date__range=[from_date,to_date],payment_status='Complete')
            if sales_report:
                sales_report_serializer = JobCardSerializer(sales_report,many=True)
                return Response(sales_report_serializer.data)
            else:
                return Response({"status":"no reports available"})
        else:
            return Response({"status":"non-authorized"})

#still didnt got idea what items to fetch
class Notifications(APIView):
    def get(self,request):
        
        return Response({"status":"go sent data her"})

class RaiseTicket(APIView,):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        ticket_id = request.query_params['ticket_id']
        ticket = Tickets.objects.get(id=ticket_id)
        if ticket:
            ticket_serializer = TicketsSerializer(ticket,many=False)
            return Response(ticket_serializer.data)
        else:
            return Response({"status":"no tickets"})

    def post(self,request):
        jobcard_id = request.data['jobcard_id']
        subject = request.data['subject']
        message = request.data['message']
        client_id = JobCard.objects.get(id=jobcard_id).vehicle.client
        Tickets.objects.create(client=client_id,subject=subject,message=message)
        return Response({'status':'woo'})

class CloseTicket(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        ticket = Tickets.objects.all()
        if ticket:
            ticket_serializer = TicketsSerializer(ticket,many=True)
            return Response(ticket_serializer.data)
        else:
            return Response({'status':'No tickets right now'})

    def put(self,request):
        ticket_id = request.data['ticket_id']
        replay = request.data['replay']
        replay_attachments = request.FILES['attachments']
        close_ticket = Tickets.objects.get(id=ticket_id)
        print(replay,'hhhe')
        close_ticket.replay = replay
        close_ticket.attachments = replay_attachments
        close_ticket.status = True
        close_ticket.save()
        return Response({"status":"ticket Closed"})

#admin ONly
class Invoicing(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user = UserDetails.objects.get(user=request.user)
        permissions = check_permissionz(user)
        if permissions['acces_granted'] == True:
            invoices = JobCard.objects.filter(payment_status='Complete')
            if invoices:
                job_card_serializer = JobCardSerializer(invoices,many=True)
                return Response(job_card_serializer.data)
            else:
                return Response({"status":'no invoices'})
        else:
            return Response({"status":"non-authorized"})