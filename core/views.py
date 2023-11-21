from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {'pessoas': pessoas, 'pessoa':''})

def salvar(request):
    rNome = request.POST.get("nome")
    rEmail = request.POST.get("email")
    rIdade = int(request.POST.get("idade"))
    Pessoa.objects.create(nome = rNome, email = rEmail, idade = rIdade)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {'pessoas':pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id = id)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {'pessoa':pessoa, 'pessoas':pessoas})

def update(request, id):
    pessoa = Pessoa.objects.get(id = id)
    pessoa.nome = request.POST.get("nome")
    pessoa.email = request.POST.get("email")
    pessoa.idade = int(request.POST.get("idade"))
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id = id)
    pessoa.delete()
    return redirect(home)