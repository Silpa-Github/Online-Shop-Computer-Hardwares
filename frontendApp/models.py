from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email_id=models.EmailField(max_length=100,null=True,blank=True)
    Message=models.TextField(max_length=100,null=True,blank=True)
class LoginDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email_id=models.EmailField(max_length=100,null=True,blank=True)
    password1=models.CharField(max_length=100,null=True,blank=True)
    password2=models.CharField(max_length=100,null=True,blank=True)
class CartDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Productname=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)

class CheckoutDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    total=models.IntegerField(null=True,blank=True)