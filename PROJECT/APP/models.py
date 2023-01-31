from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.


class customer(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField(blank=True,null=True)
    phnum=models.BigIntegerField(blank=True,null=True)
    email=models.EmailField(default="vish@gmail.com")
    profile_pic=models.ImageField(upload_to="images/%y/%m/%d",blank=True,null=True)
    state=models.CharField(max_length=100,blank=True)
    district=models.CharField(max_length=100,blank=True)

class User(AbstractUser):
    phone_number=models.CharField(max_length=13, blank=True)
    state=models.TextField(max_length=150 , blank=True)
    district=models.TextField(max_length=150 , blank=True)
    pincode=models.TextField(null=True,blank=True)
    
    date_of_birth=models.CharField(max_length=100,blank=True)
    bio=models.CharField(max_length=500, blank=True)
    profile_pic=models.ImageField(upload_to='images',blank=True)

mode=[('COD','Cash On Delivery')]

class Order(models.Model):
    country=models.TextField(max_length=150 , blank=True)
    state=models.TextField(max_length=150 , blank=True)
    district=models.TextField(max_length=150 , blank=True)
    town=models.TextField(max_length=150 , blank=True)
    H_No=models.TextField(max_length=150 , blank=True)
    pincode=models.IntegerField( blank=True)
    payment_method=models.CharField(max_length=150 , blank=True,choices=mode)