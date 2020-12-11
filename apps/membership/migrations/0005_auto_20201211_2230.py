# Generated by Django 3.1.3 on 2020-12-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_auto_20201211_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='allow_viewing_basic_image',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='allow_viewing_premium_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='membership',
            name='basic_photo_height',
            field=models.IntegerField(choices=[(100, 100), (200, 200), (400, 400), (500, 500), (800, 800), (1024, 1024), (2048, 2048), (4096, 4096)], default=200),
        ),
    ]
