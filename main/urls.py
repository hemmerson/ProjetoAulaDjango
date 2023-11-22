from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoa_fisica/lista/', views.listaPessoaFisica, name='lista_pessoa_fisica'),
    path('pessoa_fisica/novo/', views.novoPessoaFisica, name='novo_pessoa_fisica'),
    path('pessoa_fisica/update/<int:id>/', views.updatePessoaFisica, name='update_pessoa_fisica'),
    path('pessoa_fisica/delete/<int:id>/', views.deletePessoaFisica, name='delete_pessoa_fisica'),

    path('pessoa_juridica/lista/', views.listaPessoaJuridica, name='lista_pessoa_juridica'),
    path('pessoa_juridica/novo/', views.novoPessoaJuridica, name='novo_pessoa_juridica'),
    path('pessoa_juridica/update/<int:id>/', views.updatePessoaJuridica, name='update_pessoa_juridica'),
    path('pessoa_juridica/delete/<int:id>/', views.deletePessoaJuridica, name='delete_pessoa_juridica'),
]