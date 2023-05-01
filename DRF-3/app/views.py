from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
from django.http import HttpResponse , JsonResponse
from app.models import Students
from app.serializers import StudentsSerializer
from rest_framework.renderers import JSONRenderer

# De serialization 
# data back convert to the complex data type 

def home(request):
    st=Students.objects.get(id=1)
    # For all data we use many=True
    serailizer=StudentsSerializer(st )
    
    # json_data=JSONRenderer().render(serailizer.data)
    
    
    # return HttpResponse(json_data , content_type = 'application/json')

    # the other way is serializer.data here we don't need to JsonRender 
    return JsonResponse(serailizer.data)



