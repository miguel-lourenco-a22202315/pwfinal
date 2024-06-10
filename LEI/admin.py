from django.contrib import admin

from .models import Curso, Area_Cientifica, Disciplina, Projeto, LinguagemDeProgramacao, Docente

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'objetivos', 'competencias')
    search_fields = ('nome',)

class Area_CientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class LinguagemDeProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'curricularunitreadablecode', 'area_cientifica')
    search_fields = ('nome', 'curricularunitreadablecode','ano')
    filter_horizontal = ('docentes', 'linguagens')

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao', 'conceitos_aplicados', 'tecnologias_utilizadas', 'imagem','imagem','link_git')
    search_fields = ('descricao', 'conceitos_aplicados', 'tecnologias_utilizadas')
    filter_horizontal = ('linguagens',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Area_Cientifica, Area_CientificaAdmin)
admin.site.register(LinguagemDeProgramacao, LinguagemDeProgramacaoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
