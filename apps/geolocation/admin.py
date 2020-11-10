from django.contrib import admin
from .models import GeoLocation, UserUrl

# Register your models here.
models_list = [GeoLocation, UserUrl]
admin.site.register(models_list)
