# Generated by Django 2.0.5 on 2018-09-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
