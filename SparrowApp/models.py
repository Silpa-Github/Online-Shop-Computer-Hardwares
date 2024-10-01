from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    item=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to='category image',null=True,blank=True)
    description = models.TextField(max_length=50, null=True, blank=True)
class Productdb(models.Model):
    category=models.CharField(max_length=50,null=True,blank=True)
    product_name=models.CharField(max_length=50,null=True,blank=True)
    company=models.CharField(max_length=50,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    image1=models.ImageField(upload_to='product images',null=True,blank=True)
    image2=models.ImageField(upload_to='product images',null=True,blank=True)
    image3=models.ImageField(upload_to='product images',null=True,blank=True)
    specification = models.TextField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=50, null=True, blank=True)


