from django.contrib import admin
from app.views import LCStudentApi , RUDStudentApi 

from django.urls import path , include 
from rest_framework import DefaultRouter

router = DefaultRouter() 

router.regidter('')

urlpatterns = [
    path('admin/', admin.site.urls),
]
