# Generated by Django 3.1.3 on 2020-12-11 22:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20201211_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='basic_image',
            field=models.ImageField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
