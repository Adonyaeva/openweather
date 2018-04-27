from django.shortcuts import render
from .models import Weather
from urllib.request import urlopen
import json
import time

def get_weather(request):
    request_city = request.GET['city']
    if len(request_city) > 0:
        weather_list = Weather.objects.filter(city=request_city)
        weather = weather_list[0]
        if not weather or time.time() - weather.last_update.timestamp() < 1800:
            responce = urlopen("http://api.openweathermap.org/data/2.5/weather?q="+request_city+'&&APPID=8818cf47694e3fabc2f6040dffd52ee0')
            result = json.loads(responce.read())
            weather = result

        return render(request, 'api/get_weather.html', {'weather':  weather})
    else:
        return render(request, 'api/get_error.html', {})
