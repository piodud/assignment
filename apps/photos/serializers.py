from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    last_modified = serializers.DateTimeField(read_only=True)
    enterprise_image = serializers.SerializerMethodField(read_only=True)
    premium_image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'owner', 'enterprise_image', 'premium_image', 'basic_image', 'last_modified']

    def get_enterprise_image(self, obj):
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.user.groups.filter(
                name__in=['Premium', 'Enterprise']).exists():
            return request.build_absolute_uri(obj.enterprise_image.url)
        return 'Not available. Please upgrade to Enterprise Plan.'

    def get_premium_image(self, obj):
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.user.groups.filter(
                name__in=['Premium', 'Enterprise']).exists():
            return request.build_absolute_uri(obj.premium_image.url)
        return 'Not available. Please upgrade to Premium or Enterprise Plan.'
