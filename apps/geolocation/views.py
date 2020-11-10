from .models import GeoLocation, UserUrl
from .serializers import GeoLocationSerializer, UserSerializer, UserUrlSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUrlList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserUrl.objects.all()
    serializer_class = UserUrlSerializer

    def perform_create(self, serializer):
        instance = serializer.save(reporter=self.request.user)
        geolocation = GeoLocation(user_geolocation=instance, latitude=1.1, longitude=2.2)
        geolocation.save()

    # def post(self, request):
    #     serializer = UserUrlSerializer(data=request.data)
    #     print(serializer.is_valid())
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUrlDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a geo_instance instance.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserUrl.objects.all()
    serializer_class = UserUrlSerializer
    # def get_object(self, pk):
    #     try:
    #         return UserUrl.objects.get(pk=pk)
    #     except UserUrl.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk):
    #     user_url_instance = self.get_object(pk)
    #     serializer = UserUrlSerializer(user_url_instance)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     user_url_instance = self.get_object(pk)
    #     serializer = UserUrlSerializer(user_url_instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     user_url_instance = self.get_object(pk)
    #     user_url_instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class GeoLocationList(APIView):
    """
    List all geo_instances, or create a new geo_instance.
    """

    def get(self, request):
        geo_instances = GeoLocation.objects.all()
        serializer = GeoLocationSerializer(geo_instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GeoLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeoLocationDetail(APIView):
    """
    Retrieve, update or delete a geo_instance instance.
    """

    def get_object(self, pk):
        try:
            return GeoLocation.objects.get(pk=pk)
        except GeoLocation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        geo_instance = self.get_object(pk)
        serializer = GeoLocationSerializer(geo_instance)
        return Response(serializer.data)

    def put(self, request, pk):
        geo_instance = self.get_object(pk)
        serializer = GeoLocationSerializer(geo_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        geo_instance = self.get_object(pk)
        geo_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
