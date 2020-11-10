from django.contrib.auth.models import User
from rest_framework import serializers

from .models import GeoLocation, UserUrl


class UserSerializer(serializers.ModelSerializer):
    urls = serializers.PrimaryKeyRelatedField(many=True, queryset=UserUrl.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'urls']


class UserUrlSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')
    # geolocations = serializers.PrimaryKeyRelatedField(many=True, queryset=GeoLocation.objects.all())
    last_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserUrl
        fields = ['reporter', 'url', 'last_modified']

    # def create(self, validated_data):
    #     print(validated_data)
    #     """
    #     """
    #     return UserUrl.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.url = validated_data.get('url', instance.url)
    #     instance.save()
    #     return instance


class GeoLocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    continent = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=20)
    country = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=50)
    region = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=50)
    city = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=50)
    last_modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `GeoLocationSerializer` instance, given the validated data.
        """
        return GeoLocation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `GeoLocationSerializer` instance, given the validated data.
        """
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.continent = validated_data.get('continent', instance.continent)
        instance.country = validated_data.get('country', instance.country)
        instance.region = validated_data.get('region', instance.region)
        instance.city = validated_data.get('city', instance.city)

        instance.save()
        return instance
