from django.contrib import admin
from app.models import Students
# Register your models here.

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display=['id' ,'name' , 'age' , 'created_at' ,'updated_at']
