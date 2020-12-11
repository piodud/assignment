from rest_framework import generics, permissions

from .models import Image
from .serializers import ImageSerializer


class ImageList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ImageDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
