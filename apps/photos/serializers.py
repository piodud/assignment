from rest_framework import serializers

from .models import Image
from apps.membership.models import UserMembership


def get_user_membership(request):
    if request and hasattr(request, "user"):
        user_membership_qs = UserMembership.objects.filter(user=request.user)
        if user_membership_qs.exists():
            return user_membership_qs.first().membership
    return None


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    last_modified = serializers.DateTimeField(read_only=True)
    enterprise_image = serializers.SerializerMethodField(read_only=True)
    premium_image = serializers.SerializerMethodField(read_only=True)
    temp_link = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = '__all__'

    def get_enterprise_image(self, obj):
        request = self.context.get("request")
        membership = get_user_membership(request)
        if membership and membership.allow_viewing_original_image:
            return request.build_absolute_uri(obj.enterprise_image.url)
        return 'Not available. Please upgrade to Enterprise Plan.'

    def get_premium_image(self, obj):
        request = self.context.get("request")
        membership = get_user_membership(request)
        if membership and membership.allow_viewing_premium_image:
            return request.build_absolute_uri(obj.premium_image.url)
        return 'Not available. Please upgrade to Premium or Enterprise Plan.'

    def get_temp_link(self, obj):
        request = self.context.get("request")
        membership = get_user_membership(request)
        if membership and membership.generating_temp_link:
            return 'ToDo: auto-expiring url'
        return 'Not available. Please upgrade to Premium or Enterprise Plan.'
