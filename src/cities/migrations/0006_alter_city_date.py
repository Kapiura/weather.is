# Generated by Django 4.1.7 on 2023-04-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0005_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
