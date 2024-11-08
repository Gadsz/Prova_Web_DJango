"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Adicionar o "include" nesta parte, não se esquecer.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/exercicios/', include('exercicios.urls')), # Não se esquecer nome do app no path que será inserido do aplicativo. NÃO SE ESQUECER DO BARRA NO FINAL!!!
]

# Cada app criado no projeto Django é necessário que seja criado o nome dele aqui dentro.
# Neste caso o "path('api/', include('exercicios.urls'))," foi criado um caminho para o Insomnia.