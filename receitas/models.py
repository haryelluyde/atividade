from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"

class Receita(models.Model):
    nome = models.CharField(max_length=45)
    tempo_preparo = models.CharField("Tempo de preparo", max_length=45)
    modo_preparo = models.TextField("Modo de preparo")
    rendimento = models.IntegerField("Rendimento")
    autor = models.ForeignKey(Autor)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "receita"
        verbose_name_plural = "receitas"

class Ingrediente(models.Model):
    descricao = models.CharField(max_length=45)
    receita = models.ForeignKey(Receita)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "ingrediente"