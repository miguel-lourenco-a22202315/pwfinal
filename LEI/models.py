from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return f"Curso: {self.nome}\nApresentação: {self.apresentacao}\nObjetivos: {self.objetivos}\nCompetências: {self.competencias}\n"

class Area_Cientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"Área Científica: {self.nome}"

class LinguagemDeProgramacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"Linguagem de Programação: {self.nome}"

class Docente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"Docente: {self.nome}"


class Projeto(models.Model):
    nome = models.CharField(max_length=100, null=True)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_utilizadas = models.TextField()
    imagem = models.ImageField(upload_to='projetos')
    link_video = models.URLField()
    link_git = models.URLField()
    linguagens = models.ManyToManyField(LinguagemDeProgramacao, related_name='projetos')

    def __str__(self):
        return f"Projeto: {self.descricao}\nConceitos Aplicados: {self.conceitos_aplicados}\nTecnologias Utilizadas: {self.tecnologias_utilizadas}\nImagem: {self.imagem}\nLink do Vídeo: {self.link_video}\nLink do Git: {self.link_git}\n"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano =  models.CharField(max_length=100)
    semestre = models.CharField(max_length=100)
    ects =  models.CharField(max_length=100)
    curricularunitreadablecode = models.CharField(max_length=100)
    area_cientifica = models.ForeignKey(Area_Cientifica, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente)
    linguagens = models.ManyToManyField(LinguagemDeProgramacao)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    projetos = models.ManyToManyField(Projeto)
    imagem = models.ImageField(upload_to='projetos', null = True )
    def __str__(self):
        return f"Disciplina: {self.nome}\nAno: {self.ano}\nSemestre: {self.semestre}\nECTS: {self.ects}\nCódigo Curricular: {self.curricularunitreadablecode}\nÁrea Científica: {self.area_cientifica}\n"

