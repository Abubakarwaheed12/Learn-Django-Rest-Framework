from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
from django.http import HttpResponse , JsonResponse
from .models import Students
from app.serializers import StudentsSerializer
from rest_framework.renderers import JSONRenderer
import io 
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt

# De serialization 
# data back convert to the complex data type 
# by using bytes io 


@csrf_exempt
def home(request):
    
    if request.method=='POST':
        post_data=request.body
        stream=io.BytesIO(post_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentsSerializer( data=python_data ) 
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created i table'}
            # json_data=JSONRenderer().render(res)
             
            # return HttpResponse(json_data , content_type='application/json')
            
            # Shortcut
            return JsonResponse(res)
        
        # json_data=JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data , content_type='application/json')
        
        return JsonResponse(serializer.error)

   

