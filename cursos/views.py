from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Estudante
from .forms import CursoForm, EstudanteForm

# Curso Views

def home(request):
    return render(request, 'home.html')

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

def criar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    
    return render(request, 'criar_curso.html', {'form': form})

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'editar_curso.html', {'form': form})

def excluir_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')  

    return render(request, 'excluir_curso.html', {'curso': curso})

def listar_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'listar_estudantes.html', {'estudantes': estudantes})

def criar_estudante(request):
    if request.method == "POST":
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudantes')
    else:
        form = EstudanteForm()
    
    return render(request, 'criar_estudante.html', {'form': form})

def editar_estudante(request, id):
    estudante = Estudante.objects.get(id=id)
    if request.method == "POST":
        form = EstudanteForm(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudantes')
    else:
        form = EstudanteForm(instance=estudante)

    return render(request, 'editar_estudante.html', {'form': form})

def excluir_estudante(request, id):
    estudante = Estudante.objects.get(id=id)
    if request.method == "POST":
        estudante.delete()
        return redirect('listar_estudantes')
    return render(request, 'excluir_estudante.html', {'estudante': estudante})
