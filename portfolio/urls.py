from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('me',views.me, name='me'),
    path('PW',views.PW, name='PW'),
]
