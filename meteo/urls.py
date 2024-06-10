from django.urls import path
from . import views
urlpatterns = [
      path('tempo/', views.previsao_meteorologica, name='tempo'),
      path('tempo5dias/', views.previsao_meteorologica5, name='tempo'),
      path('lista_cidades/', views.lista_cidades, name='lista_cidades'),
      path('listaporcidades/<str:cidade_id>/<str:nomeciade>', views.previsao_meteorologicacidade, name='lista_cidades2'),
      path('cidades/', views.cidades, name='cidades'),
      path('api/lista_cidades/', views.lista_cidades_api, name='lista_cidades_api'),
      path('api/previsao_hoje/<str:cidade_id>/', views.previsao_hoje_api, name='previsao_hoje_api'),
      path('api/previsao_5dias/<str:cidade_id>/', views.previsao_5dias_api, name='previsao_5dias_api'),
      path('api/', views.api_documentation, name='api_documentation'),
]