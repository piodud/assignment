import os

import requests
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.response import Response

from .models import GeoLocation, UserUrl
from .serializers import GeoLocationSerializer, UserSerializer, UserUrlSerializer


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUrlList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserUrl.objects.all()
    serializer_class = UserUrlSerializer

    def create(self, request, *args, **kwargs):
        address = request.data.get('ip_or_url')
        geolocation_data, error_msg = IpStackApi.send_request(address)
        if error_msg:
            return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)

        geoloc_serializer = GeoLocationSerializer(data={**geolocation_data})
        geoloc_serializer.is_valid(raise_exception=True)
        try:
            instance = UserUrl.objects.get(reporter=request.user,
                                           ip_or_url=address)
        except UserUrl.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save(reporter=self.request.user)

        geoloc_serializer.save(user_geolocation=instance)
        headers = self.get_success_headers(geoloc_serializer.data)
        return Response(geoloc_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserUrlDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a geo_instance instance.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserUrl.objects.all()
    serializer_class = UserUrlSerializer


class GeoLocationList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer

    def perform_create(self, serializer):
        serializer.save(user_geolocation=self.request.user)


class GeoLocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a geo_instance instance.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer


class IpStackApi:
    IPSTACK_ADDRESS = 'http://api.ipstack.com/'
    TOKEN = os.getenv("IPSTACK_TOKEN")

    @classmethod
    def send_request(cls, address):
        address = f'{cls.IPSTACK_ADDRESS}/{address}?access_key={cls.TOKEN}'
        try:
            response = requests.post(address)
            return cls.unpack(response.json())
        except requests.exceptions.ConnectionError:
            err_message = {"ip_or_url": 'Could not reach geolocation api. Try again later.'}
            return None, err_message

    @classmethod
    def validate_results(cls, results):
        if results['latitude'] and results['latitude']:
            return results, None
        else:
            err_message = {"ip_or_url": 'Could not obtain geolocation data from address. '
                                        'Check whether address is correct.'}
            return None, err_message

    @classmethod
    def unpack(cls, results):
        results = {'latitude': results.get('latitude'),
                   'longitude': results.get('longitude'),
                   'continent': results.get('continent_name'),
                   'country': results.get('country_name'),
                   'region': results.get('region_name'),
                   'city': results.get('city'), }
        return cls.validate_results(results)
