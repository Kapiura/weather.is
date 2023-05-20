from django.db import models

class swieta(models.Model):
    descritpion = models.CharField(max_length=1000)
    date = models.CharField(max_length=50)