from io import BytesIO

from PIL import Image as PILImage
from django.core.files import File
from django.core.validators import FileExtensionValidator
from django.db import models


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
        self.basic_image = resize_image(self.enterprise_image, (4096, 200))
        self.premium_image = resize_image(self.enterprise_image, (4096, 400))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['last_modified']
