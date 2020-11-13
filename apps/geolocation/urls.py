from django.urls import path

from . import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),

    path('address', views.UserUrlList.as_view()),
    path('address/<int:pk>', views.UserUrlDetail.as_view()),

    path('geolocations', views.GeoLocationList.as_view()),
    path('geolocations/<int:pk>', views.GeoLocationDetail.as_view()),
]
