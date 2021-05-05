from django.contrib import admin
from  workshope.models import Client,Vehicle,VehicleType,JobCard,VehicleRemarks,UserDetails
# Register your models here.

admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(JobCard)
admin.site.register(VehicleRemarks)
admin.site.register(UserDetails)