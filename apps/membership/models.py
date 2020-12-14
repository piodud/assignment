from django.conf import settings
from django.db import models

MEMBERSHIP_CHOICES = (
    ('Basic', 'basic'),
    ('Premium', 'premium'),
    ('Enterprise', 'enterprise')
)

PHOTO_HEIGHTS = (
    (100, 100),
    (200, 200),
    (400, 400),
    (500, 500),
    (800, 800),
    (1024, 1024),
    (2048, 2048),
    (4096, 4096),
)


class Membership(models.Model):
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, default='Basic',
        max_length=30
    )
    basic_photo_height = models.IntegerField(choices=PHOTO_HEIGHTS, default=200)
    premium_photo_height = models.IntegerField(choices=PHOTO_HEIGHTS, default=400)

    allow_viewing_original_image = models.BooleanField(default=False)
    allow_viewing_premium_image = models.BooleanField(default=False)

    generating_temp_link = models.BooleanField(default=False)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
