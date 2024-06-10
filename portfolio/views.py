import requests
from django.shortcuts import render

def index(request):
   forecast_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
   weather_type_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

   #
   forecast_response = requests.get(forecast_url)
   forecast_response.raise_for_status()
   forecast_data = forecast_response.json()


   weather_type_response = requests.get(weather_type_url)
   weather_type_response.raise_for_status()
   weather_type_data = weather_type_response.json()


   tipo_tempo_id = forecast_data['data'][0]['idWeatherType']


   context = {
        'previsao': forecast_data['data'][0],
    }



   return render(request, 'portfolio/index.html', context)

def me(request):
    return render(request, 'portfolio/MeByMe.html')

def PW(request):
    return render(request, 'portfolio/pw.html')