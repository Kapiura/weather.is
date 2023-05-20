from django.db import models

# Create your models here.

class horoscope(models.Model):
    sign = models.CharField(max_length=100)
    description = models.CharField(max_length=50000)