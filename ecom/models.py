from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth  import forms

# Create your models here.
class header_top(models.Model):
  email=models.EmailField()
  phone=models.CharField(max_length=1000)
  
class header_middle(models.Model):
   logo=models.ImageField(upload_to="logo")
   
class carousel_inner(models.Model):
   title=models.CharField(max_length=200)
   desc=models.TextField()
   img=models.ImageField(upload_to='carousel')
   price=models.ImageField(upload_to='price')
   
class brands(models.Model):
   name=models.CharField(max_length=100)
  

  
class Category(models.Model):
  name= models.CharField(max_length=150)
    
  def __str__(self):
    return self.name
    
class Subcategory(models.Model):
    name=models.CharField(max_length=150)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.name
    
class Product(models.Model):
   category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
   sub_category=models.ForeignKey(Subcategory,on_delete=models.CASCADE,default=None)
   img= models.ImageField(upload_to='ecommerce/product')
   name=models.CharField(max_length=100)
   price=models.IntegerField()
   date=models.DateField(auto_now_add=True)
   desc=models.TextField(default='')
   featured=models.BooleanField(default=False)
   
class uercreateForm(UserCreationForm):
   email= forms.EmailField(required=True, label='Email',error_message={'exist':'Email Id already exist'})
   
   
   
   class Meta:   
      modela= User
      fields=('username','email','password1','password2')
      
   
               

