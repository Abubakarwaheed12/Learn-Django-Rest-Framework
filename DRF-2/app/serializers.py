from app.models import Students
from rest_framework import serializers

class StudentsSerializer(serializers.Serializer):
    # model=Students
    name=serializers.CharField()
    age=serializers.IntegerField()    