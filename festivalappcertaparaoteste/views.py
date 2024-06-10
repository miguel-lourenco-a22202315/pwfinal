from django.shortcuts import render
from .models import band, Localizacao, festivaiss

def festivaiss_view(request):
    context = {
        'festivaiss': festivaiss.objects.all().order_by('nome'),
    }
    return render(request, "festivalappcertaparaoteste/festivais.html", context)


def album_view(request, banda_nome):

    festival = festivaiss.objects.get(nome=banda_nome)

    context = {
        'festivaiss': festival

    }
    return render(request, "festivalappcertaparaoteste/festival.html", context)
