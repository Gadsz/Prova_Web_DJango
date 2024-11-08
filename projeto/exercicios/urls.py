from django.urls import path
from .views import ExerciciosListCreateView, TreinosListCreateView, ExerciciosReadUpdateDeleteView

# Antes de abrir o Insomnia, executar o Ctrl J para abrir terminal No VScode e executar, "pyhton3 manage.py makemigrations"
# depois "pyhton3 manage.py migrate" e posteriormente "python3 manage.py runserver".

urlpatterns = [
    path('exercicios/', ExerciciosListCreateView.as_view(), name='exercicios-list-create'), # E esse é o de exercicios, o que muda
                                                                                         #"path('NOME DA VARIÁVEL/', NOME DA VARIÁVELlistCreateView.as_view(), name='NOME DA VARIÁVEL-list-create'),"
    path('exercicios/<int:pk>/', ExerciciosReadUpdateDeleteView.as_view()), #UPDATE E DELETE
    path('treinos/', TreinosListCreateView.as_view(), name='treinos-list-create'), # Esse é o caminho para criar (CRUD) de álbum
]

# Nesta parte quando abrir o Insomnia o que será adicionado na url da new request será o nome do path que é o
# nome da view que irei trabalhar, por exemplo nesta prova, "[URL AQUI]/api/exercicios/".
# NÃO SE ESQUECER DENTRO DO INSOMNIA DE ALTERAR O BODY PARA JSON (EMBAIXO DO POST/GET/UPDATE/DELETE, SEGUNDO BOTÃO A DIREITA).