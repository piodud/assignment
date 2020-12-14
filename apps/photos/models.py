from io import BytesIO

from PIL import Image as PILImage
from django.contrib.auth.models import User
from django.core.files import File
from django.core.validators import FileExtensionValidator
from django.db import models
from apps.membership.models import Membership, UserMembership


def resize_image(image, size=(4096, 4096)):
    im = PILImage.open(image)
    im.convert('RGB')
    im.thumbnail(size)
    thumb_io = BytesIO()
    im.save(thumb_io, 'JPEG', quality=85)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail


class Image(models.Model):
    owner = models.ForeignKey('auth.User', related_name='image', on_delete=models.CASCADE)
    basic_image = models.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    premium_image = models.ImageField()
    enterprise_image = models.ImageField()
    last_modified = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.enterprise_image = resize_image(self.basic_image)
        try:
            membership = UserMembership.objects.get(user=self.owner).membership
            self.basic_image = resize_image(self.enterprise_image, (4096, membership.basic_photo_height))
            self.premium_image = resize_image(self.enterprise_image, (4096, membership.premium_photo_height))
        except UnboundLocalError as e:
            print('Cannot get get membership plan')
            raise e
        except UserMembership.DoesNotExist:
            print('Cannot convert images.')

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['last_modified']
