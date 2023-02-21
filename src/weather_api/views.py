from django.shortcuts import render
from datetime import datetime
import requests
import json

# Create your views here.

def get_weather_data(city):
    api_key = 'f5e851929409af1dd87f860f5d2cc9f9'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)


    results = {}
    results['lon'] = data['coord']['lon']
    results['lat'] = data['coord']['lat']
    results['name'] =data['name']
    results['temp'] =data['main']['temp']
    results['feels_like'] =data['main']['feels_like']
    results['humidity'] =data['main']['humidity']
    sunset = data['sys']['sunset']
    sunset_time = datetime.utcfromtimestamp(sunset).strftime('%I:%M:%S %p')
    results['sunset'] = sunset_time
    sunrise = data['sys']['sunrise']
    sunrise_time = datetime.utcfromtimestamp(sunrise).strftime('%I:%M:%S %p')
    results['sunrise'] = sunrise_time
    return results


def show(request):
    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET.get('city')
        results = get_weather_data(city)
        context ={'results': results}
    else:
        context= {}
    return render(request, 'api.html', context)



