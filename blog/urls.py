from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('todos_os_artigos/', views.todos_os_artigos, name='todos_os_artigos'),
    path('avaliacoes_do_artigo/<str:artigo_id>/', views.avaliacoes_do_artigo, name='avaliacoes_do_artigo'),
    path('artigos_do_autor/<str:autor_id>/', views.artigos_do_autor, name='artigos_do_autor'),
    path('comentarios_do_artigo/<str:artigo_id>/', views.comentarios_do_artigo, name='comentarios_do_artigo'),
    path('index/', views.index, name='index'),  # Nome da URL alterado para 'index'
    path('id/<str:artigo_id>/', views.id, name='id_artigo'),  # Nome da URL alterado para 'id_artigo'
    path('artigo/novo', views.nova_banda_view, name="nova_banda"),
    path('artigo/<str:nome>/edita/', views.edita_banda_view, name="edita_banda"),
    path('artigo/<str:nome>/apaga/', views.apaga_banda_view,name='apaga_banda'),
    path('avaliacao/novo', views.nova_musica_view, name="musicas"),
    path('avaliacao/<str:nome>/edita/', views.edita_musica_view,name="edita_musicas"),
    path('avaliacao/<str:nome>/apaga/', views.apaga_musica_view,name="apaga_musicas"),
    path('comentario/novo', views.nova_album_view, name="nova_banda"),
    path('comentario/<str:nome>/edita/', views.edita_album_view,name="edita_albuns"),
    path('comentario/<str:nome>/apaga/', views.apaga_album_view,name="apaga_albuns"),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
