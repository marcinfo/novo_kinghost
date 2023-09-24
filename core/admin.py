from django.contrib import admin
from .models import Profile, Tb_Registros, TbPragas, Tbculturas


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


@admin.register(Tb_Registros)
class Tb_OcorrenciasAdmin(admin.ModelAdmin):
    list_display = ['id_ocorrencia','ativo','usuario','cultura', 'praga','status','imagem', 'nome_propriedade',
                    'hectares', 'prejuizo', 'latitude', 'longitude', 'observacao']
    search_fields = ('id_ocorrencia', 'praga')
    ordering = ['praga']


@admin.register(TbPragas)
class TbPragasAdmin(admin.ModelAdmin):
    list_display = ['id_praga', 'especie', 'nome_comum']

@admin.register(Tbculturas)
class TbculturasAdmin(admin.ModelAdmin):
    list_display = ['id', 'cultura',]