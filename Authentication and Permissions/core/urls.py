from django.contrib import admin
from app.views import StudentApi

from django.urls import path , include 
from rest_framework.routers  import DefaultRouter

router = DefaultRouter() 

router.register('studentapi', StudentApi, basename='student')
# router.register('studentapi', StudentApi, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
