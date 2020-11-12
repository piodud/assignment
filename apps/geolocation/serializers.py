from django.contrib.auth.models import User
from rest_framework import serializers

from .models import GeoLocation, UserUrl


class UserSerializer(serializers.ModelSerializer):
    # urls = serializers.PrimaryKeyRelatedField(many=True, queryset=UserUrl.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'urls']
        depth = 1


class UserUrlSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')
    # geolocations = serializers.PrimaryKeyRelatedField(many=True, queryset=GeoLocation.objects.all())
    last_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserUrl
        fields = ['reporter', 'url', 'last_modified', 'geolocations']
        depth = 1


class GeoLocationSerializer(serializers.ModelSerializer):
    user_geolocation = serializers.ReadOnlyField(source='url')
    longitude = serializers.SerializerMethodField()

    def get_longitude(self, obj):
        print(obj)
        return 999.999

    class Meta:
        model = GeoLocation
        fields = ['user_geolocation', 'latitude', 'longitude']
