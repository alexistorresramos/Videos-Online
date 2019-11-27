from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import datetime
from datetime import date
from django import template

from django_countries.widgets import CountrySelectWidget
from django import forms

# from phonenumber_field.modelfields import PhoneNumberField
#from phonenumber_field.phonenumber import PhoneNumberField

register = template.Library()

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


#class News_Stations(models.Model):
#    media_type = models.CharField(max_length=25, blank=True)


#    class Meta:
#        verbose_name_plural = "News_stations"

#    def  __str__(self):
#        return self.category


# from upload form
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, default='1 ', verbose_name="Category", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    desc = models.TextField(max_length=255, blank=True)
    pdf = models.FileField(upload_to='books/pdfs/')
    video_watermark = models.FileField(upload_to='books/watermark/') 
    watermark_ready = models.BooleanField(default = False)   
    price = models.IntegerField()     
    price_exclusive = models.IntegerField()
    minutes_exclusive = models.IntegerField()
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
#    buyers=models.ManyToManyField('Buyer', related_name="video_buyers")
    created_at = models.DateField(default=date.today)
    incident_date = models.DateField(default=date.today)
    country = CountryField(default='US')


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class Buyer(models.Model):
    news_name=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)

# from upload form
class News(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, default='1 ', verbose_name="Category", on_delete=models.SET_DEFAULT)
    author = models.CharField(max_length=30)   
    news_station = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    desc = models.TextField(max_length=255, blank=True)
    pdf = models.FileField(upload_to='books/pdfs/')
    video_watermark = models.FileField(upload_to='books/watermark/') 
    price = models.IntegerField() 
    price_exclusive = models.IntegerField()    
    minutes_exclusive = models.IntegerField(default='0')
    purchase_date = models.DateField(default=date.today)
    incident_date = models.DateField(default=date.today) 
    country = models.CharField(max_length=30)  

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
 

class Cart(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, default='1 ', verbose_name="Category", on_delete=models.SET_DEFAULT)
    author = models.CharField(max_length=30)   
    news_station = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    desc = models.TextField(max_length=255, blank=True)
    pdf = models.FileField(upload_to='books/pdfs/')
    video_watermark = models.FileField(upload_to='books/watermark/') 
    price = models.IntegerField() 
    price_exclusive = models.IntegerField()    
    minutes_exclusive = models.IntegerField(default='0')
    purchase_date = models.DateField(default=date.today)
    incident_date = models.DateField(default=date.today)
    country = models.CharField(max_length=30) 

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.user.username
    @register.inclusion_tag('cart.html')
    def get_total(self):
        total = 0
        for order_item in self.Cart.all():
            total += order_item.price
#        if self.coupon:
#            total -= self.coupon.amount
        print('get_total')
        return total

class Videos_sold(models.Model):
    videos_to_sell = models.ManyToManyField(Book)
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,null=True,
    )

    @classmethod
    def make_friend(cls, buyer, new_video):
        videos_sold, created = cls.objects.get_or_create(
            buyer=buyer
        )
        videos_sold.video_to_sell.add(new_video)

    @classmethod
    def lose_friend(cls, buyer, new_video):
        videos_sold, created = cls.objects.get_or_create(
            buyer=buyer
        )
        videos_sold.video_to_sell.remove(new_video)

class Create_Watermark(models.Model):
    pkin = models.IntegerField()

class Sales_Factor(models.Model):
    less_10M =  models.IntegerField()
    less_50M =  models.IntegerField()
    less_100M =  models.IntegerField()    
    less_150M =  models.IntegerField()
    local_less_10M =  models.IntegerField()
    local_less_50M =  models.IntegerField()
    local_less_100M =  models.IntegerField()    
    local_less_150M =  models.IntegerField()


class User_Info(models.Model):
    news_name=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    address = models.CharField(max_length=50, null=True, blank=True)
    address1 = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=25, null=False, blank=True)
    city = models.CharField(max_length=25, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)    
    phone2 = models.CharField(max_length=25, null=True, blank=True)  
#    phone = PhoneNumberField(null=False, blank=False, unique=True)    
#    phone2 = PhoneNumberField(null=True, blank=True, unique=True)  
    active = models.IntegerField(default=-1)

class News_Type(models.Model):
    news_type = models.CharField(max_length=25, blank=True)

    class Meta:
        verbose_name_plural = "News_Types"

    def  __str__(self):
        return self.news_type


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    type_news = models.ForeignKey(News_Type, default='1 ', verbose_name="News_Type", on_delete=models.SET_DEFAULT)
    web = models.CharField(max_length=50, null=True, blank=True)
    alt_email= models.EmailField(max_length=70, null= True, unique= True)
    country = CountryField(default='US')

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, null=True, blank=False)    
    type_news = models.ForeignKey(News_Type, default='1 ', verbose_name="News_Type", on_delete=models.SET_DEFAULT)
    web = models.CharField(max_length=50, null=True, blank=True)
    alt_email= models.EmailField(max_length=70, null= True, unique= True)
    country = CountryField(default='US')
    if_seller = models.BooleanField(default = False)     

    def _str_(self):
        return self.user.username

# from upload form


class Account(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=30)   
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    desc = models.TextField(max_length=255, blank=True)
    price = models.IntegerField() 
    transacion_date = models.DateField(default=date.today)
    book_id = models.CharField(max_length=100)
    news_id = models.CharField(max_length=100)
    incident_date = models.DateField(default=date.today)
    country = models.CharField(max_length=30) 
#    if_seller = models.BooleanField(default = False)  


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.user.username
    @register.inclusion_tag('cart.html')
    def get_total(self):
        total = 0
        for order_item in self.Cart.all():
            total += order_item.price
#        if self.coupon:
#            total -= self.coupon.amount
        print('get_total')
        return total


class Country(models.Model):
    country = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"

    def  __str__(self):
        return self.country

#class Videos_sold(models.Model):
#    videos_to_sell = models.ManyToManyField(Book)
#    buyer = models.ForeignKey(
#        settings.AUTH_USER_MODEL,
#        on_delete=models.CASCADE,null=True,
#    )
#################
