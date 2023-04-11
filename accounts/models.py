from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    image=models.ImageField(upload_to='images')


class Notes(models.Model):
    title = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=100,null=False)
    rating = models.CharField(max_length=5,null=False)

 

