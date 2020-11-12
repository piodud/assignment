from django.db import models
from django.contrib.auth.models import User


class UserUrl(models.Model):
    reporter = models.ForeignKey('auth.User', related_name='urls', on_delete=models.CASCADE)
    url = models.URLField()


class GeoLocation(models.Model):
    user_geolocation = models.ForeignKey(UserUrl, related_name='geolocations', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    continent = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_modified']
