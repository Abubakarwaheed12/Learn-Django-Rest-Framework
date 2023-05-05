from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    father_name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=20)
    grade =models.CharField(max_length=20)
    
    
    def  __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Our Students'