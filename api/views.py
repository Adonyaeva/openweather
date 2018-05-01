from django.shortcuts import render
from .models import Weather
from urllib.request import urlopen, URLError
import json
import time
from django.utils import timezone


def weather(request):
    request_city = request.GET['city']
    if len(request_city) > 0:
        weather_exist = Weather.objects.filter(city=request_city)
        if not weather_exist:
            weather_city = get_weather(request_city)
            if weather_city:
                Weather.objects.create(city=request_city, temperature=weather_city['temperature'], pressure=weather_city['pressure'],
                                   wind_speed=weather_city['wind_speed'], last_update=timezone.now())
            else:
                return render(request, 'api/get_error.html', {})
        else:
            if (time.time() - weather_exist[0].last_update.timestamp()) > 1800:
                weather_city = get_weather(request_city)
                weather_exist[0].temperature = weather_city['temperature']
                weather_exist[0].pressure = weather_city['pressure']
                weather_exist[0].wind_speed = weather_city['wind_speed']
                weather_exist[0].update()
            else:
                weather_city = weather_exist[0]

        return render(request, 'api/get_weather.html', {'weather':  weather_city})
    else:
        return render(request, 'api/get_error.html', {})


def get_weather(city):
    try:
        res = urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q=" + city + '&&units=metric&&APPID=8818cf47694e3fabc2f6040dffd52ee0')
        result = json.loads(res.read())
        pressure = result.get('main').get('pressure') // 1.333
        return {'city': city, 'temperature': result.get('main').get('temp'), 'pressure': pressure,
                'wind_speed': result.get('wind').get('speed')}
    except URLError:
        return False

