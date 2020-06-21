from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # city = 
    phone_number = models.CharField(max_length=15)
    image  = models.ImageField(upload_to='profile/')



class City(models.Model):
    name = models.CharField(max_length=length, ${blank=True, null=True})