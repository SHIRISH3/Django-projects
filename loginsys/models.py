from django.db import models

# Create your models here.
class Newuser(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=1)
    martialstatus=models.CharField(max_length=100)
