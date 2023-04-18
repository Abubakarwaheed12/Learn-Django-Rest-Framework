from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        
    

class MyModel(BaseModel):
    item_name=models.CharField(max_length=300)
    
    def __str__(self):
        return self.item_name
    
    class Meta:
        verbose_name_plural = "App Model "
    