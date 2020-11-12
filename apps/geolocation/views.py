from .models import GeoLocation, UserUrl
from .serializers import GeoLocationSerializer, UserSerializer, UserUrlSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth.models import User


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

    def perform_create(self, serializer):
        try:
            print('Exists')
            instance = UserUrl.objects.get(reporter=self.request.user, url=serializer.validated_data.get('url'))
        except UserUrl.DoesNotExist:
            instance = serializer.save(reporter=self.request.user)
            print('Does not exist')
        geolocation = GeoLocationSerializer(user_geolocation=instance, latitude=1.1, longitude=2.2)
        geolocation.save()


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
