from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle , ScopedRateThrottle
from rest_framework.filters import SearchFilter , OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .models import Students 
from .serializers  import StudentSerializer
# Create your views here.

class StudentApi(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    # Throttling 
    # throttle_classes = [UserRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

    # Search 
    filter_backends = [SearchFilter]
    search_fields = ['name']
    # multiple
    # search_fields = ['name','age']
    # start with 
    search_fields = ['^name']


    def get_queryset(self):
        queryset = super().get_queryset() 
        parameter_value = self.request.query_params.get('parameter_name')
        if parameter_value:
            queryset = queryset.filter(your_field=parameter_value)
        self.queryset = Students.objects.filter()