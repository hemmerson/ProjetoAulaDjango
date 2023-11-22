from django.shortcuts import render, redirect, get_object_or_404
from .models import PessoaFisica, PessoaJuridica
from .forms import PessoaFisicaForm, PessoaJuridicaForm

# Create your views here.
def index(request):
    return render(request, 'index_main.html')

def listaPessoaFisica(request):
    listaPF = PessoaFisica.objects.all()
    return render(request, 'pf_list.html', {'listapessoafisica': listaPF})

def novoPessoaFisica(request):
    if request.method == 'POST':
        form = PessoaFisicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listaPessoaFisica)
    
    else:
        form = PessoaFisicaForm()
    return render(request, 'pf_form.html', {'form':form})

def updatePessoaFisica(request, id):
    pessoaFisica = get_object_or_404(PessoaFisica, id=id)

    if request.method == 'POST':
        form = PessoaFisicaForm(request.POST, instance=pessoaFisica)
        if form.is_valid():
            form.save()
            return redirect(listaPessoaFisica)
    else:
        form = PessoaFisicaForm(instance=pessoaFisica)
    
    return render(request, 'pf_form.html', {'form':form, 'pessoa_fisica':pessoaFisica})

def deletePessoaFisica(request, id):
    pessoaFisica = get_object_or_404(PessoaFisica, id = id)

    if request.method == 'POST':
        pessoaFisica.delete()
        return redirect(listaPessoaFisica)
    
    return render(request, 'pf_confirm_delete.html', {'pessoa_fisica':pessoaFisica})

# ================= Pessoa Jurídica ================================
def listaPessoaJuridica(request):
    listaPJ = PessoaJuridica.objects.all()
    return render(request, 'pj_list.html', {'listapessoajuridica': listaPJ})

def novoPessoaJuridica(request):
    if request.method == 'POST':
        form = PessoaJuridicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listaPessoaJuridica)
    
    else:
        form = PessoaJuridicaForm()
    return render(request, 'pj_form.html', {'form':form})

def updatePessoaJuridica(request, id):
    pessoaJuridica = get_object_or_404(PessoaJuridica, id = id)

    if request.method == 'POST':
        form = PessoaJuridicaForm(request.POST, instance=pessoaJuridica)
        if form.is_valid():
            form.save()
            return redirect(listaPessoaJuridica)
    else:
        form = PessoaJuridicaForm(instance=pessoaJuridica)
    
    return render(request, 'pj_form.html', {'form':form, 'pessoa_juridica':pessoaJuridica})

def deletePessoaJuridica(request, id):
    pessoaJuridica = get_object_or_404(PessoaJuridica, id = id)

    if request.method == 'POST':
        pessoaJuridica.delete()
        return redirect(listaPessoaJuridica)
    
    return render(request, 'pj_confirm_delete.html', {'pessoa_juridica':pessoaJuridica})
