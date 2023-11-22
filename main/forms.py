from django import forms
from .models import PessoaFisica, PessoaJuridica

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = '__all__'
        widgets = {
            'nome':forms.TextInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
            'cpf':forms.TextInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
            'data_nascimento':forms.TextInput(attrs={
                'type':'date',
                'class':'form-control',
                'required':'required',
            }),
        }

class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = '__all__'
        widgets = {
            'nome':forms.TextInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
            'cnpj':forms.TextInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
            'razao_social':forms.TextInput(attrs={
                'class':'form-control',
                'required':'required',
            }),
        }