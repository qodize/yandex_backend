# Generated by Django 3.1.7 on 2021-03-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_courier_assign_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='earnings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='courier',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
