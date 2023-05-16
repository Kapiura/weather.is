from django.db import models

class cities(models.Model):
    name = models.CharField(max_length=100)

class city(models.Model):
    city_id = models.IntegerField()
    date = models.CharField(max_length=50)
    temp = models.FloatField(default=0)
    description_simple = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=300, default='')
    air_pol = models.FloatField(default=0)
    so2 = models.FloatField()
    no = models.FloatField(default=0)
    no2 = models.FloatField()
    o3 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    co = models.FloatField()
    nh3 = models.FloatField()
    id_weather = models.IntegerField(default=0)
    pic = models.CharField(default='', max_length=150)
    wind_speed = models.FloatField(default=0)
    clouds = models.CharField(default='',max_length=150)
    rain = models.FloatField()
    sunrise = models.IntegerField(default=0)
    sunset = models.IntegerField(default=0)
    timezone = models.IntegerField(default=0)
    #s
    humidity = models.FloatField(default=0)
    sea_level = models.IntegerField(default=0)
    grnd_level = models.IntegerField(default=0)