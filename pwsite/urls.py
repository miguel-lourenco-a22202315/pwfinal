# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.index_potatos, name='sobre'),
    path('HTML/', views.index_HTML, name='interesses'),

]