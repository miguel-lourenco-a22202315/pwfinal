# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('benfica/', views.index_benfica, name='benfica'),
    path('sorpting/', views.index_sporting, name='sporting'),
    path('porto/', views.index_porto, name='porto'),

]