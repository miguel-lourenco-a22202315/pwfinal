# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('tropa/',views.index_tropa),
    path('benfica/',views.index_popa),
    path('chigomoedas/',views.index_toto),
]