from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', views.salvar, name='salvar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='deletar'),
]