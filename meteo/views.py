import requests
from django.shortcuts import render

def previsao_meteorologica(request):

    forecast_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    weather_type_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    # Obter a previsão
    forecast_response = requests.get(forecast_url)
    forecast_response.raise_for_status()  # Verificar se a resposta é bem-sucedida
    forecast_data = forecast_response.json()

    # Obter as classes de tempo
    weather_type_response = requests.get(weather_type_url)
    weather_type_response.raise_for_status()  # Verificar se a resposta é bem-sucedida
    weather_type_data = weather_type_response.json()

    # Filtrar o tipo de tempo correspondente
    tipo_tempo_id = forecast_data['data'][0]['idWeatherType']

    tipo_tempo = None
    # Percorre os dados do tipo de tempo para encontrar o correspondente ao tipo_tempo_id
    for item in weather_type_data['data']:
        if item['idWeatherType'] == tipo_tempo_id:
            tipo_tempo = item
            break


    context = {
        'previsao': forecast_data['data'][0],
        'tipo_tempo': tipo_tempo,
    }

    return render(request, 'meteo/tempo.html', context)







def previsao_meteorologica5(request):
    if request.method == 'POST':
        cidade_selecionada = request.POST.get('cidade_selecionada')

        if cidade_selecionada:

            cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
            cities_response = requests.get(cities_url)
            cities_response.raise_for_status()
            cities_data = cities_response.json()
            cidades = {cidade['local']: cidade['globalIdLocal'] for cidade in cities_data['data']}


            forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidades[cidade_selecionada]}.json'


            forecast_response = requests.get(forecast_url)
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()
                return render(request, 'meteo/tempo5.html', {'previsao': forecast_data['data'][:5], 'cidades': cidades, 'cidade_selecionada': cidade_selecionada})
            else:
                return render(request, 'meteo/tempo5.html', {'erro': 'Erro ao obter a previsão meteorológica'})
        else:
            return render(request, 'meteo/tempo5.html', {'erro': 'Por favor, selecione uma cidade'})
    else:
        cidades = lista_cidades()
        return render(request, 'meteo/tempo5.html', {'cidades': cidades})


def lista_cidades():

    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'


    cities_response = requests.get(cities_url)
    cities_response.raise_for_status()
    cities_data = cities_response.json()

    # Extrair os nomes das cidades e seus IDs
    cidades = {cidade['local']: cidade['globalIdLocal'] for cidade in cities_data['data']}

    return cidades


def previsao_meteorologicacidade(request, cidade_id,nomeciade):
    nome= nomeciade

    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'


    forecast_response = requests.get(forecast_url)
    forecast_response.raise_for_status()
    forecast_data = forecast_response.json()


    weather_type_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    weather_type_response = requests.get(weather_type_url)
    weather_type_response.raise_for_status()
    weather_type_data = weather_type_response.json()

    # Filtrar o tipo de tempo correspondente para os próximos 5 dias
    tipo_tempo_ids = [day['idWeatherType'] for day in forecast_data['data'][:5]]
    tipo_tempo = {}

    # Percorrer os dados do tipo de tempo para encontrar os correspondentes aos tipo_tempo_ids
    for item in weather_type_data['data']:
        if item['idWeatherType'] in tipo_tempo_ids:
            tipo_tempo[item['idWeatherType']] = item

    # Adicionar descrição do tipo de tempo aos dados da previsão meteorológica
    for day in forecast_data['data'][:5]:
        tipo_tempo_id = day.get('idWeatherType')
        if tipo_tempo_id in tipo_tempo:
            day['tipo_tempo_descricao'] = tipo_tempo[tipo_tempo_id].get('descWeatherTypePT')
        else:
            day['tipo_tempo_descricao'] = None


    context = {
        'previsao': forecast_data['data'][:5],
        'cidade': nome
    }

    return render(request, 'meteo/tempoporcidade.html', context)




def cidades(request):

    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'


    cities_response = requests.get(cities_url)
    cities_response.raise_for_status()
    cities_data = cities_response.json()

    # Extrair os nomes das cidades e seus IDs
    cidades = {cidade['local']: cidade['globalIdLocal'] for cidade in cities_data['data']}


    return render(request, 'meteo/lidadecidades.html', {'cidades': cidades})

















from django.http import JsonResponse


def lista_cidades_api(request):

    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cities_response = requests.get(cities_url)
    cities_response.raise_for_status()
    cities_data = cities_response.json()

    # Extrair os nomes das cidades e seus IDs
    cidades = {cidade['local']: cidade['globalIdLocal'] for cidade in cities_data['data']}

    return JsonResponse(cidades)

def previsao_hoje_api(request, cidade_id):

    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'


    weather_type_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'


    forecast_response = requests.get(forecast_url)
    if forecast_response.status_code != 200:
        return JsonResponse({'erro': 'Erro ao obter a previsão meteorológica'})

    forecast_data = forecast_response.json()
    previsao_hoje = forecast_data['data'][0]  # Obter a previsão para hoje


    weather_type_response = requests.get(weather_type_url)
    weather_type_response.raise_for_status()
    weather_type_data = weather_type_response.json()


    tipo_tempo_id = previsao_hoje['idWeatherType']

    tipo_tempo = None
    # Percorre os dados do tipo de tempo para encontrar o correspondente ao tipo_tempo_id
    for item in weather_type_data['data']:
        if item['idWeatherType'] == tipo_tempo_id:
            tipo_tempo = item
            break

    # Obter o nome da cidade correspondente ao globalIdLocal na previsão meteorológica
    cidade_id_previsao = forecast_data['globalIdLocal']
    cidade = None

    distritos_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    distritos_response = requests.get(distritos_url)
    distritos_data = distritos_response.json()

    for cidade_item in distritos_data['data']:
        if cidade_item['globalIdLocal'] == cidade_id_previsao:
            cidade = cidade_item
            break


    previsao_hoje_data = {
        'nome_cidade': cidade['local'],
        'data': previsao_hoje['forecastDate'],
        'temperatura_minima': previsao_hoje['tMin'],
        'temperatura_maxima': previsao_hoje['tMax'],
        'descricao_tempo': tipo_tempo['descWeatherTypePT'],
        'precipitacao': previsao_hoje['precipitaProb'],
        'icone_tempo': f'https://www.ipma.pt/bin/icons/weather-type-{previsao_hoje["idWeatherType"]}.svg'
    }
    return JsonResponse(previsao_hoje_data)

def previsao_5dias_api(request, cidade_id):

    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'


    weather_type_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'


    forecast_response = requests.get(forecast_url)
    if forecast_response.status_code != 200:
        return JsonResponse({'erro': 'Erro ao obter a previsão meteorológica'})

    forecast_data = forecast_response.json()
    previsoes = forecast_data['data'][:5]  # Obter as previsões para os próximos 5 dias


    weather_type_response = requests.get(weather_type_url)
    weather_type_response.raise_for_status()  # Verificar se a resposta é bem-sucedida
    weather_type_data = weather_type_response.json()


    cidade_id_previsao = forecast_data['globalIdLocal']
    cidade = None

    distritos_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    distritos_response = requests.get(distritos_url)
    distritos_data = distritos_response.json()

    for cidade_item in distritos_data['data']:
        if cidade_item['globalIdLocal'] == cidade_id_previsao:
            cidade = cidade_item
            break

    previsoes_data = []
    for previsao in previsoes:
        tipo_tempo_id = previsao['idWeatherType']
        tipo_tempo = None
        # Percorre os dados do tipo de tempo para encontrar o correspondente ao tipo_tempo_id
        for item in weather_type_data['data']:
            if item['idWeatherType'] == tipo_tempo_id:
                tipo_tempo = item
                break

        previsao_data = {
            'nome_cidade': cidade['local'],
            'data': previsao['forecastDate'],
            'temperatura_minima': previsao['tMin'],
            'temperatura_maxima': previsao['tMax'],
            'descricao_tempo': tipo_tempo['descWeatherTypePT'],
            'precipitacao': previsao['precipitaProb'],
            'icone_tempo': f'https://www.ipma.pt/bin/icons/weather-type-{previsao["idWeatherType"]}.svg'
        }
        previsoes_data.append(previsao_data)

    return JsonResponse(previsoes_data, safe=False)




def api_documentation(request):
    return render(request, 'meteo/api.html')




