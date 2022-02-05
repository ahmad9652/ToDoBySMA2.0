from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class task(models.Model):
    sno = models.AutoField(primary_key=True)
    Task = models.CharField(max_length=30)
    Task_Description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    Time =models.DateTimeField(auto_now_add=True)
class contactuser(models.Model):
    Name = models.CharField(max_length=30) 
    Address=models.CharField(max_length=50)
    Description = models.CharField(max_length=30)
    Email=models.EmailField()
    Time=models.DateTimeField(auto_now_add=True)
# class 