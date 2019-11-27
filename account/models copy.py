from django.db import models

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


# from upload form
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

#################
     