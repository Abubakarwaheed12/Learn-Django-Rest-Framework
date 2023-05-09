from django.shortcuts import render
from app.models import Students
from app.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Permission Classes

class StudentApi(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class = StudentSerializer
    
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]


