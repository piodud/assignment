from django.contrib.auth.models import User
from .models import GeoLocationData
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class GeoLocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocationData
        fields = ['user', 'ip', 'url', 'latitude', 'longitude', 'local_time', 'is_proxy',
                  'isp', 'continent', 'country', 'region', 'zip', 'created_at', 'last_modified']
