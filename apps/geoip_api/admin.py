from django.contrib import admin
from .models import GeoLocationData

# Register your models here.
models_list = [GeoLocationData]
admin.site.register(models_list)
