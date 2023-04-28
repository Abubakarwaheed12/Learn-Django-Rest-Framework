from django.shortcuts import render 
from django.http import HttpResponse , JsonResponse
from app.models import Students
from app.serializers import StudentsSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.

#func base  

def home(request):
    st=Students.objects.get(id=1)
    # For all data we use many=True
    serailizer=StudentsSerializer(st )
    
    # json_data=JSONRenderer().render(serailizer.data)
    
    
    # return HttpResponse(json_data , content_type = 'application/json')

    # the other way is serializer.data here we don't need to JsonRender 
    return JsonResponse(serailizer.data)


# for list of dictionaries 
def home(request):
    st=Students.objects.all()
    # For all data we use many=True
    serailizer=StudentsSerializer(st , many =True)
    
    # json_data=JSONRenderer().render(serailizer.data)
    
    
    # return HttpResponse(json_data , content_type = 'application/json')

    # the other way is serializer.data here we don't need to JsonRender 
    return JsonResponse(serailizer.data , safe=False)
