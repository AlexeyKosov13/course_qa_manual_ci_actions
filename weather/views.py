import requests
from django.http import JsonResponse
from django.shortcuts import render

API_KEY = 'cbd884be8dfaeb7549452e820c2f3476'

def get_weather(request):
    city = request.GET.get('city', 'Moscow')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
        }
        return JsonResponse(weather_info)
    return JsonResponse({'error': 'City not found'}, status=404)

def weather_page(request):
    return render(request, 'weather/index.html')
