from django.shortcuts import render
from .models import Weather

def get_weather(request):
    request_city = request.GET["city"]
    # if len(request.city) > 0
    city_weather = Weather.objects.filter(city=request_city)

    return render(request, 'api/get_weather.html', {'weather': city_weather})
