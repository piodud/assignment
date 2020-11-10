import os
from django.core.management import execute_from_command_line
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()
    import io
    from apps.geolocation.serializers import GeoLocationSerializer
    from apps.geolocation.models import GeoLocation, UserUrl
    from django.contrib.auth.models import User
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser

    user = User.objects.get(username='admin')
    data = {'user': None, 'url': "http://192.168.1.1"}
    instance = UserUrl(**data)
    instance.save()



    # geoloc = GeoLocation.objects.all()
    # for g in geoloc:
    #     print(g.id,g.ip)
    #
    # g10 = GeoLocation.objects.get(id=10)
    # g10 = GeoLocationSerializer(g10)
    # print(g10.data)
    # content = JSONRenderer().render(g10.data)
    # print(content)
    # stream = io.BytesIO(content)
    # data = JSONParser().parse(stream)
    # data.pop('id')
    # data.pop('url')
    # print(data)
    #
    # serializer = GeoLocationSerializer(data=data)
    # serializer.is_valid(raise_exception=True)
    # print(serializer.is_valid())
    # # True
    # print(serializer.validated_data)
    # serializer.save()
