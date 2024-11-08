from django.db import models

# Nesta aba será inserido as entidades do projeto, cada entidade é uma classe que
# separa as partes do projeto, neste exemplo está sendo usado 2 classes sendo elas
# "Exercicios" e "Treinos".

from django.db import models

# Inicio do Exercicios;
# (TUDO ISSO VAI NO JSON QUANDO EXECUTADO VIA INSONMIA).

class Exercicios(models.Model):
    nome = models.CharField(max_length=255) # Nome do exercício.
    descricao_execucao = models.CharField(max_length=100) # Descricação do exercício obrigatória.

    def __str__(self):
        return self.nome

# Inicio do Treinos;
# (TUDO ISSO VAI NO JSON QUANDO EXECUTADO VIA INSONMIA).

class Treinos(models.Model):
    data_inicio = models.CharField(max_length=255) # Inicio dos treinos (obrigatório);
    data_fim = models.CharField(max_length=255) # Fim dos treinos (obrigatório);
    objetivo = models.CharField(max_length=255) # Objetivo dos treinos (obrigatório);
    exercicios = models.ForeignKey(Exercicios, on_delete=models.CASCADE) # Exercicios com chave estrangeira para não repetir.

    def __str__(self):
        return self.titulo

# É possível adicionar mais classes conforme a complexidade do projeto.