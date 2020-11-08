from django.contrib.auth.models import User
from .models import GeoLocationData
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GeoLocationDataSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GeoLocationDataViewSet(viewsets.ModelViewSet):
    queryset = GeoLocationData.objects.all()
    serializer_class = GeoLocationDataSerializer
    # permission_classes = [permissions.IsAuthenticated]

