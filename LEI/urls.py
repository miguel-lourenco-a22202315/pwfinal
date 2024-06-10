from django.urls import path
from .views import curso_page, disciplina_page, projeto_page,projetos
from . import views
urlpatterns = [
    path('curso/<str:curso_nome>/', curso_page, name='curso'),
    path('disciplina/<str:disciplina_id>/', disciplina_page, name='disciplina'),
    path('projeto/<str:projeto_nome>/<str:nome>/', projeto_page, name='projeto'),
    path('projetos/<str:disciplina_nome>/', projetos, name='projetos'),
    path('curso/novo', views.nova_banda_view, name="nova_banda"),
    path('curso/<str:nome>/edita/', views.edita_banda_view, name="edita_banda"),
    path('curso/<str:nome>/apaga/', views.apaga_banda_view,name='apaga_banda'),
    path('disciplina/novo', views.nova_album_view, name="musicas"),
    path('disciplina/<str:nome>/edita/', views.edita_album_view,name="edita_musicas"),
    path('disciplina/<str:nome>/apaga/', views.apaga_album_view,name="apaga_musicas"),
    path('projeto/<str:nome>/novo', views.nova_musica_view, name="nova_banda"),
    path('projeto/<str:nome>/<str:nome2>/edita/', views.edita_musica_view,name="edita_albuns"),
    path('projeto/<str:nome>/<str:nome2>/apaga/', views.apaga_musica_view,name="apaga_albuns"),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
