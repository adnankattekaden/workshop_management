from django.db import models

# Create your models here.

    
class Client(models.Model):
    name = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=10)
    place = models.CharField(max_length=50)
    addres = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

class VehicleType(models.Model):
    name = models.CharField(max_length=50)
    blueprint_image = models.FileField(upload_to='blueprint')


class Vehicle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=50)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
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

    datetime = models.DateTimeField()
    job_card_types = models.CharField(max_length=15,choices=job_card_types)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


    Remarks = models.ManyToManyField(VehicleRemarks)
    tracking_id = models.CharField(max_length=50)
    estimate_amount = models.FloatField()
    spares_realted_info = models.ManyToManyField(SparesInformation)
    job_status = models.CharField(max_length=25,choices=job_status_options)
    payment_status = models.CharField(max_length=30,default='pending')



