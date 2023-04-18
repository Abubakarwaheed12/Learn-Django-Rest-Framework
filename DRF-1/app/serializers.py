from app.models import MyModel
from rest_framework import serializers



class MyModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=MyModel
        fields=['uid' ,'item_name' , 'created_at']
        
        