# Generated by Django 3.1.3 on 2020-11-08 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoLocationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('url', models.URLField(null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('local_time', models.DateTimeField()),
                ('is_proxy', models.BooleanField()),
                ('isp', models.CharField(blank=True, max_length=50)),
                ('continent', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('region', models.CharField(blank=True, max_length=50)),
                ('zip', models.CharField(blank=True, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['last_modified'],
            },
        ),
    ]
