from django.db import models
from django.contrib.auth.models import User


class GeoLocationData(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ip = models.GenericIPAddressField()
    url = models.URLField(null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    local_time = models.DateTimeField()
    is_proxy = models.BooleanField()
    isp = models.CharField(max_length=50, blank=True)
    continent = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=10, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_modified']




