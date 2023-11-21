from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=80)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nome} {self.email} {self.idade}'