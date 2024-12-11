from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="estudantes")

    def __str__(self):
        return self.nome
