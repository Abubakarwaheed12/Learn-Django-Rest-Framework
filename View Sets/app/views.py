from django.shortcuts import render
from app.models import Students
from app.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import Response 
from rest_framework import status

