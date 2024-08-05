from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Escala
from ..forms import EscalaForm  # Importe seu formulário EscalaForm adequado aqui

@login_required
def visualizar_escala_col(request):
    escalas = Escala.objects.all()
    form = EscalaForm()  # Crie uma instância do formulário vazio
    
    if request.method == 'POST':
        form = EscalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_colaborador')
    
    return render(request, 'consulta_colaborador/consulta_escala_col.html', {'escalas': escalas, 'form': form})