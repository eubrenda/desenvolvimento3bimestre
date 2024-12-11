from django.contrib import admin
from django.urls import path, include
from cursos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Adicionando a URL para a página inicial
    path('cursos/', include('cursos.urls')),  # As URLs dos cursos
    path('estudantes/', include('cursos.urls')),  # As URLs dos estudantes
]
