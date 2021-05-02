from django.urls import path
from . import views

urlpatterns = [
    path('create-client/', views.ClientDetails.as_view(),name='client-profile')
]
