from django.urls import path
from workshope import views

urlpatterns = [
    path('create-client/', views.CreateClientDetails.as_view(),name='client_profile'),
    path('edit-client/<int:id>/', views.EditClientDetails.as_view(),name='edit_client_profile'),
    path('create-vehicle/', views.CreateVehicleDetaills.as_view(),name='create_vehicle'),
    path('edit-vehicle/<int:id>/',views.EditVehicleDetaills.as_view(),name='edit_vehicle'),
    path('create-job-card/', views.CreateJobCard.as_view(),name='create_job_card'),
    path('edit-job-card/<int:id>/',views.EditJobCard.as_view(),name='edit_JobCard'),
    path('add-spares/<int:id>/',views.SparesInformationView.as_view(),name='add_spares'),
    path('tracking/<str:tracking_id>/',views.TrackingView.as_view(),name='tracking_view'),
    
]
