from django.shortcuts import render
from rest_framework import routers , serializers , viewsets , permissions
from app.serializers import MyModelSerializer
from app.models import MyModel
# Create your views here.

class MyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyModel.objects.all().order_by('-created_at')
    serializer_class = MyModelSerializer
    permission_classes = [permissions.IsAuthenticated]


