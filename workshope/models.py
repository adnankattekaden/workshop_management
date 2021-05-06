from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    roles = (
        ('admin','admin'),
        ('staff','staff'),
    )
    
    permissions = models.CharField(max_length=20,choices=roles)

class Client(models.Model):
    name = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=10)
    place = models.CharField(max_length=50)
    addres = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

class VehicleType(models.Model):
    vehicle_types = (
        ('Car','Car'),
        ('Bike','Bike'),
    )
    name = models.CharField(max_length=50,choices=vehicle_types)
    blueprint_image = models.FileField(upload_to='blueprint')

class Vehicle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=20)

class VehicleRemarksAttachments(models.Model):
    attachments = models.FileField(upload_to='attchments')

class VehicleRemarks(models.Model):
    x_coordinates = models.FloatField()
    y_coordinates = models.FloatField()
    notes = models.TextField()
    attachments = models.ManyToManyField(VehicleRemarksAttachments)

class SparesInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.FloatField()


class JobCard(models.Model):

    job_card_types = (
        ('Mechanical','Mechanical'),
        ('Detailing','Detailing'),
    )

    job_status_options = (
        ('Received','Received'),
        ('Doing','Doing'),
        ('Outsourced','Outsourced'),
        ('Completed','Completed'),
        ('Delivered','Delivered'),
    )

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    job_card_types = models.CharField(max_length=15,choices=job_card_types)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    remarks = models.ManyToManyField(VehicleRemarks)
    tracking_id = models.CharField(max_length=50)
    estimate_amount = models.FloatField()
    spares_realted_info = models.ManyToManyField(SparesInformation)
    job_status = models.CharField(max_length=25,choices=job_status_options)
    payment_status = models.CharField(max_length=30,default='pending')


class Tickets(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    subject = models.CharField(max_length=25)
    message = models.TextField()
    replay = models.TextField(blank=True)
    attachments = models.FileField(blank=True,upload_to='replay_attachments')
    status = models.BooleanField(default=False)



