from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    num = models.CharField( max_length=50)