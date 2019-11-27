from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100) 
    img = models.ImageField(upload_to='pics')  
    desc = models.TextField()
    price = models.IntegerField() 
    offer = models.BooleanField(default=False)
  
class Document1(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)