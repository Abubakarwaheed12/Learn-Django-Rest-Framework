from django.shortcuts import render
from app.models import Students
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin
from app.serializers import StudentSerializer  

# Create your views here.

# Class
# get all students and create students class  
class LCStudentApi(GenericAPIView , CreateModelMixin , ListModelMixin):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer
    
    def get(self , request , *args , **kwargs ):
        
        return self.list(request , *args , **kwargs)
    
    def post(self ,request , *args , **kwargs):
        
        return self.create(request , *args , **kwargs)
    
    
class RUDStudentApi(GenericAPIView , UpdateModelMixin , DestroyModelMixin , RetrieveModelMixin):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer 
    
    def get(self ,request , *args , **kwargs):

        return self.retrieve(request , *args , **kwargs)
    
    def put(self , request , *args , **kwargs):
        
        return self.update(request , *args , **kwargs)
    
    def delete(self , request , *args , **kwargs):
        
        return self.destroy(request , *args , **kwargs)