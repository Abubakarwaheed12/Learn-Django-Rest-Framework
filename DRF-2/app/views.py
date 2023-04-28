from django.shortcuts import render 
from django.http import HttpResponse
from app.models import Students
from app.serializers import StudentsSerializer
from rest_framework.renderers import JSONRender 
# Create your views here.

#func base 

def stu(request):
    st=Students.objects.get(id=1)
    serailizer=StudentsSerializer(st)
    json_data=JSONRender().render(serailizer.data)
    
    
    return HttpResponse(json_data , content_type = 'application/json')

