from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Escala
from ..forms import EscalaForm  # Importe seu formulário EscalaForm adequado aqui

@login_required
def visualizar_escala(request):
    escalas = Escala.objects.all()
    form = EscalaForm()  # Crie uma instância do formulário vazio
    
    if request.method == 'POST':
        form = EscalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultar_escala')
    
    return render(request, 'consulta_colaborador/consulta_escala.html', {'escalas': escalas, 'form': form})

@login_required
def deletar_consulta_escala(request, pk):
    escala = get_object_or_404(Escala, id=pk)
    
    if request.method == 'POST':
        escala.delete()
        return redirect('consultar_escala')
    
    return render(request, 'consulta_escala/delete_consulta_escala.html', {'escala': escala})
