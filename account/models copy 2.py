from django.db import models
from django.conf import settings

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100) 
    img = models.ImageField(upload_to='pics')  
    desc = models.TextField()
    price = models.IntegerField() 
    offer = models.BooleanField(default=False)

class Destination2(models.Model):
    name = models.CharField(max_length=100) 
    img = models.ImageField(upload_to='pics')  
    desc = models.TextField()
    price = models.IntegerField() 
    offer = models.BooleanField(default=False)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    category = models.CharField(max_length=25, blank=True)
    category_cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def  __str__(self):
        return self.category

# from upload form
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, default='1', verbose_name="Category", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    desc = models.TextField(max_length=255, blank=True)
    pdf = models.FileField(upload_to='books/pdfs/')
    video_watermark = models.FileField(upload_to='books/watermark/')    
    price = models.IntegerField()     
    price_exclusive = models.IntegerField()
    minutes_exclusive = models.IntegerField()
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

#################
     