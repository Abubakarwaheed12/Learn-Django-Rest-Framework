from django.contrib import admin
from django.urls import path
from app.views import TodoAPI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , TodoAPI.as_view()),
]
