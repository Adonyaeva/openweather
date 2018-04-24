from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^weather$', views.get_weather, name='get_weather'),
]