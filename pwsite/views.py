# pwsite/views.py

from django.shortcuts import render

def index_view(request):
    return render(request, "pwsite/index.html")


def index_potatos(request):
    return render(request, "pwsite/sobre.html")

def index_HTML(request):
    return render(request,"pwsite/interesses.html")