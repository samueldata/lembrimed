from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.morador_listar, name='morador_listar'),
    re_path(r'^editar/(?P<pcpf>\d+)/$', views.morador_editar, name='morador_editar'),
    re_path(r'^cadastrar/$', views.morador_cadastrar, name='morador_cadastrar'),
    #Salva novo morador ou morador existente
    re_path(r'^salvar/$', views.morador_salvar, name='morador_salvar'),
    re_path(r'^excluir/(?P<pcpf>\d+)/$', views.morador_excluir, name='morador_excluir'),
]