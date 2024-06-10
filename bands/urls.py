from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('musica/<str:album_nome>/', views.musicas_view, name='musicas_url'),
    path('album/<str:banda_nome>/', views.album_view, name='album_url'),
    path('banda/<str:nome>/', views.banda_view, name='banda_url'),
    path('bandas/', views.bandas_view, name='bandas_url'),
    path('banda/novo', views.nova_banda_view, name="nova_banda"),
    path('banda/<str:nome>/edita/', views.edita_banda_view, name="edita_banda"),
    path('banda/<str:nome>/apaga/', views.apaga_banda_view,name='apaga_banda'),
    path('musicas/<str:titulo>/novo', views.nova_musica_view, name="musicas"),
    path('musicas/<str:nome>/<str:nomealbum>/edita/', views.edita_musica_view, name="edita_musicas"),
    path('musicas/<str:nome>/<str:nomealbum>/apaga/', views.apaga_musica_view,name="apaga_musicas"),
    path('albuns/<str:nomebanda>/novo', views.nova_album_view, name="nova_banda"),
    path('albuns/<str:nome>/<str:nomebanda>/edita/', views.edita_album_view,name="edita_albuns"),
    path('albuns/<str:nome>/<str:nomebanda>/apaga/', views.apaga_album_view,name="apaga_albuns"),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]


