from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/novo/', views.criar_curso, name='criar_curso'),
    path('cursos/<int:id>/editar/', views.editar_curso, name='editar_curso'),
    path('cursos/<int:id>/excluir/', views.excluir_curso, name='excluir_curso'),
    path('estudantes/', views.listar_estudantes, name='listar_estudantes'),
    path('estudantes/novo/', views.criar_estudante, name='criar_estudante'),
    path('estudantes/<int:id>/editar/', views.editar_estudante, name='editar_estudante'),
    path('estudantes/<int:id>/excluir/', views.excluir_estudante, name='excluir_estudante'),
]
