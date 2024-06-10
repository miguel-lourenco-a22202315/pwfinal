from django.urls import path
from . import views

app_name = 'festival'

urlpatterns = [
    path('festivais/', views.festivaiss_view),
    path('festival/<str:banda_nome>/', views.album_view),
]
