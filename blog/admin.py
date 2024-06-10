from django.contrib import admin

# Register your models here.
from  .models import Autor
from  .models import Artigo
from  .models import Comentario
from  .models import Avaliacao




class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade')
    ordering= ('nome', 'idade')
    search_fields = ('nome', 'idade' )

admin.site.register(Autor,AutorAdmin)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conteudo','data_publicacao','autor')
    ordering= ('titulo', 'autor','data_publicacao')
    search_fields = ('titulo', 'autor' )

admin.site.register(Artigo,ArtigoAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'artigo','data_comentario','autor')
    ordering= ('artigo', 'data_comentario')
    search_fields = ('autor', 'artigo' )


admin.site.register(Comentario,ComentarioAdmin)

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('autor', 'artigo','pontuacao')
    ordering= ('pontuacao', 'artigo', 'autor')
    search_fields = ('autor', 'artigo' )







admin.site.register(Avaliacao,AvaliacaoAdmin)