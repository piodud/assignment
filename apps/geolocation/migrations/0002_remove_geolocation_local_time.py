# Generated by Django 3.1.3 on 2020-11-09 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geolocation',
            name='local_time',
        ),
    ]
