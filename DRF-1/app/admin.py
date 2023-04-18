from django.contrib import admin
from app.models import MyModel
# Register your models here.

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display=['uid' , 'item_name' , 'created_at' , 'updated_at']


