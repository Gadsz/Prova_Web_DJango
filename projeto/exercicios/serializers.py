# Serializers eu preciso criar junto com as urls.py dentro do nome do projeto em que estou criando
# Neste caso, "exercicios" (clicar na pasta em si e posteriormente em cima em novo arquivo para evitar
# que seja criado no lugar errado).

from rest_framework import serializers
from .models import Exercicios, Treinos

class ExerciciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicios
        fields = '__all__'

class TreinosSerializer(serializers.ModelSerializer):
    exercicios = ExerciciosSerializer(read_only=True) # Já realiza a busca do objeto exercicios ao inves do id
    class Meta:
        model = Treinos
        fields = '__all__' # Generico sem campos, somente o nome do exercício.