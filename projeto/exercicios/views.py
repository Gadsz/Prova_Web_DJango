from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Você precisa importar os models neste contexto o "Exercicios" e "Treinos" pois são os únicos 2 models neste exemplo.

from .models import Exercicios, Treinos

#  Você precisa importar os serializers neste contexto o "ExerciciosSerializer" e "TreinosSerializer" pois são os únicos 2 models neste exemplo.

from .serializers import ExerciciosSerializer, TreinosSerializer

# EXEMPLO 1 DE EXERCICIO FUNCIONAL;
# AS VIEWS É O CRUD DENTRO DO INSOMNIA.

class ExerciciosListCreateView(APIView):
    def post(self, request):
        serializer = ExerciciosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Consultar depois mas estava "exercicioss" com 2 s.

    def get(self, request):
        exercicio = Exercicios.objects.all()
        serializer = ExerciciosSerializer(exercicio, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# EXEMPLO PARA DAR GET DA CHAVE PRIMÁRIA, DAR UPDATE DELETE (UD DO CRUD)

class ExerciciosReadUpdateDeleteView(APIView):
    def get(self, request, pk):
        exercicios = get_object_or_404(Exercicios, pk=pk)
        serializer = ExerciciosSerializer(exercicios)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        exercicios = get_object_or_404(Exercicios, pk=pk)
        serializer = ExerciciosSerializer(exercicios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        exercicios = get_object_or_404(Exercicios, pk=pk)
        exercicios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# EXEMPLO 1 DE TREINO FUNCIONAL;
# AS VIEWS É O CRUD DENTRO DO INSOMNIA.

class TreinosListCreateView(APIView):
    def post(self, request):
        serializer = TreinosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# "treinoss" estava com 2 s se der problema testar com apenas com treino

    def get(self, request):
        treinos = Treinos.objects.all()
        serializer = TreinosSerializer(treinos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)