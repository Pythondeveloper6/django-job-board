from django.db import models

# Create your models here.

'''
 django model field : 
    - html widget

'''
class Job(models.Model):  # table 
    title = models.CharField(max_length=100)  # column