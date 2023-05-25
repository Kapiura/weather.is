from django.db import models

# Create your models here.
class Shopping_sundays(models.Model):
    date = models.CharField(max_length=11)

class Holidays(models.Model):
    descritpion = models.CharField(max_length=1000)
    date = models.CharField(max_length=50)