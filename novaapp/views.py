# pwsite/views.py

from django.shortcuts import render

def index_benfica(request):
    return render(request, "novaapp/benfica.html")


def index_sporting(request):
    return render(request, "novaapp/sporting.html")

def index_porto(request):
    return render(request,"novaapp/porto.html")