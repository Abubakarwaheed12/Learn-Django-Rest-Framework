from django.shortcuts import render
from app.models import Students
from app.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Permission Classes

# class StudentApi(viewsets.ModelViewSet):
#     queryset=Students.objects.all()
#     serializer_class = StudentSerializer


# ReadOnly ModelViewSet

class StudentApi(viewsets.ReadOnlyModelViewSet):
    queryset=Students.objects.all()
    serializer_class = StudentSerializer


# class StudentApi(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Students.objects.all()
#         serializer = StudentSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Students.objects.get(id=pk)
#         serializer = StudentSerializer(queryset)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer=StudentSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response({'msg':'saved successfully'})
        
#         return Response(serializer.errors)

  

#     def update(self, request, pk=None):
#         pass
    

#     def partial_update(self, request, pk=None):
#         pass


#     def destroy(self, request, pk=None):
#         pass