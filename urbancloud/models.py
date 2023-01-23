from django.db import models

# Create your models here.

class Contactus(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(max_length=200,blank=True,null=True)

