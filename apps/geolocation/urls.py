from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('urls/', views.UserUrlList.as_view()),
    path('urls/<int:pk>/', views.UserUrlDetail.as_view()),

    path('geolocations/', views.GeoLocationList.as_view()),
    path('geolocations/<int:pk>/', views.GeoLocationDetail.as_view()),
]
