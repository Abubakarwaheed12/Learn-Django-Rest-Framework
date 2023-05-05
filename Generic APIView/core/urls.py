from django.contrib import admin
from django.urls import path
from app.views import LCStudentApi , RUDStudentApi 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', LCStudentApi.as_view()),
    path('RUDstudentapi/<int:pk>/', RUDStudentApi.as_view() )
]
