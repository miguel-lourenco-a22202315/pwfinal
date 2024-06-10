"""bandas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.contrib import admin
from django.urls import path, include   # incluir include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),  # novo path
    path('pwsite/', include('pwsite.urls')),  # novo path
    path('Benfica/', include('novaapp.urls')),  # novo path
    path('Bandas/', include('bands.urls')),  # novo path
    path('Blog/', include('blog.urls')),  # novo path
    path('Lusofona/', include('LEI.urls')),  # novo path
    path('Festivais/',include('festivalappcertaparaoteste.urls')),
    path('Login/', include('login.urls')),
    path('Meteriologia/', include('meteo.urls')),
    path('', include('portfolio.urls')),
]