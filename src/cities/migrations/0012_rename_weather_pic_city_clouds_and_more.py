# Generated by Django 4.2 on 2023-04-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0011_city_weather_description_simple_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='weather_pic',
            new_name='clouds',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='weather_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='weather_description_simple',
            new_name='description_simple',
        ),
        migrations.AddField(
            model_name='city',
            name='pic',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='city',
            name='rain',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='city',
            name='sunrise',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='sunset',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='timezone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='wind_speed',
            field=models.CharField(default='', max_length=100),
        ),
    ]
