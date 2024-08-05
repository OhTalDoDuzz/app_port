from django import forms
from django.forms import ModelForm
from .models import Escala, Evento, Permissao, Colaborador, Area, Colaborador, Tipo_contrato, Cargo, Fornecedor


class EscalaForm(forms.ModelForm):
    evento_select = forms.ModelChoiceField(queryset=Evento.objects.all(), required=False, empty_label="Selecione um Evento")
    area_select = forms.ModelChoiceField(queryset=Area.objects.all(), required=False, empty_label="Selecione uma Área")
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(), required=False, empty_label="Selecione um Cargo")
    contrato = forms.ModelChoiceField(queryset=Tipo_contrato.objects.all(), required=False, empty_label="Selecione um Contrato")

    class Meta:
        model = Escala
        fields = [
            'evento_select',
            'data_evento',
            'id_colaborador',
            'area_select',
            'cargo',
            'contrato',
            'origem',
            'data_inicio',
            'data_final',
            'qtd_diaria',
            'qtd_dias_pgto',
            'unidade_diaria',
            'total_diaria',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['evento_select'].choices = [(evento.id, evento.nome) for evento in Evento.objects.all()]
        self.fields['area_select'].choices = [(area.id, area.nome) for area in Area.objects.all()]



class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'nome',
            'cidade',
            'estado',
            'data',
            'tipo',
            'sku',
        ]


class PermissaoForm(forms.ModelForm):
    class Meta:
        model = Permissao
        fields = [
            'nome',
        ]


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = [
            'nome',
            'sobrenome',
            'rg',
            'cpf',
            'telefone',
            'cidade',
            'data_nascimento'
        ]


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'name',
            'cnpj',
            'cpf',
            'servico',
        ]





