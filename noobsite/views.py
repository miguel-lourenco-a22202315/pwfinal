# noobsite/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_tropa(request):
    return HttpResponse("O Panda ´é FIXEEEEEE")

def index_popa(request):
    return HttpResponse("tou farto deste semestre")


def index_toto(request):
    return HttpResponse("O sporting ´é a nossa ?")