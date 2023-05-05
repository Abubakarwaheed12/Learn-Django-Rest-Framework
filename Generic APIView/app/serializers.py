from app.models import Students 
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Students
        fields = ['id' ,'name' , 'age' ,'father_name' ,'class_name','grade']
        
    # Same Validation 
    # def validate_name(self, value):
    #     if value[0].islower():
    #         raise serializers.ValidationError('name always start with Capital letter ') 
            