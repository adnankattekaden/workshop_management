from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from . serializers import *

# Create your views here.

class Test(APIView):
    def get(self,request):
        return Response({"status":"WOOW"})