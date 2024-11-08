from django.shortcuts import render

# Parte analisado da views.py do exemplo "biblioteca" do professor

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Você precisa importar os models neste contexto o "Artista" e "Album" pois são os únicos 2 models neste exemplo

from .models import Artista, Album
#  Você precisa importar os serializers neste contexto o "ArtistaSerializer" e "AlbumSerializer" pois são os únicos 2 models neste exemplo

from .serializers import ArtistaSerializer, AlbumSerializer

# EXEMPLO 1 DE ARTISTA FUNCIONAL
# AS VIEWS SÃO OS POST E GET DENTRO DO INSOMNIA

class ArtistaListCreateView(APIView):
    def post(self, request):
        serializer = ArtistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        artistas = Artista.objects.all() # Correção sem Serializer
        # artistas = ArtistaSerializer.objects.all() --- Errei nesta parte colocando o Serializer após Artista (ArtistaSerializer)
        serializer = ArtistaSerializer(artistas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# EXEMPLO 1 DE ALBUM FUNCIONAL
# AS VIEWS SÃO OS POST E GET DENTRO DO INSOMNIA

class AlbumListCreateView(APIView):
    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        albums = Album.objects.all() # CORREÇÃO
        # albums = AlbumSerializer.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
