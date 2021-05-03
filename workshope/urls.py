from django.urls import path
from workshope import views

urlpatterns = [
    path('create-client/', views.CreateClientDetails.as_view(),name='client_profile'),
    path('edit-client/<int:id>/', views.EditClientDetails.as_view(),name='edit_client_profile'),
    path('create-vehicle/', views.CreateCarDetaills.as_view(),name='create_vehicle'),
    

]
