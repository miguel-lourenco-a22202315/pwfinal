import json
from LEI.models import Curso, Disciplina, Area_Cientifica

def importar_curso(ficheiro):

    Curso.objects.all().delete()
    Disciplina.objects.all().delete()
    Area_Cientifica.objects.all().delete()

    with open(ficheiro, 'r') as f:
        ola = json.load(f)

        curso = ola['courseDetail']
        area_cientificanome = curso['scientificArea']
        area_cientifica = Area_Cientifica.objects.create(nome=area_cientificanome)

        Curso.objects.create(
            nome=curso['courseName'],
            apresentacao=curso['presentation'],
            objetivos=curso['objectives'],
            competencias=curso['competences']
        )

        disciplinas = ola['courseFlatPlan']
        for disciplina in disciplinas:
            Disciplina.objects.create(
                nome=disciplina['curricularUnitName'],
                ano=disciplina['curricularYear'],
                semestre=disciplina['semester'],
                ects=disciplina['ects'],
                curricularunitreadablecode=disciplina['curricularIUnitReadableCode'],
                area_cientifica=area_cientifica
            )

ficheiro = 'LEI/json/lei.json'
importar_curso(ficheiro)
