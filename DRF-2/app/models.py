from django.db import models

# Create your models here.
class BaseModel(models.Model):
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        
    
class Students(BaseModel):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Students'