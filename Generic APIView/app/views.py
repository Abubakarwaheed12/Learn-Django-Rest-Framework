from django.shortcuts import render
from app.models import Students
from app.serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# Generic view 


@api_view(['GET','POST'])
def ApiViewMethod(request):
    if request.method =='GET':
        return Response({'msg':'Get method is called'})
    
    if request.method =='POST':
        return Response({'msg':'Post method is called' ,'data':request.data})