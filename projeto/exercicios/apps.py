from django.apps import AppConfig


class SpotifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exercicios'

# Cada app criado no projeto Django é necessário que seja criado o nome dele aqui dentro.