from django.shortcuts import render
from django.shortcuts import redirect 
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse

def cadastrar_usuario(request):
    if request.method == 'GET':
        return render(request, 'autentication/cadastro.html')
    else:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Já existe um usuário com esse username")
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=senha)
        user.save()
        return redirect(reverse('login'))
    
def login_usuario(request):
    if request.method == 'GET':
        return render(request,'autentication/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect(reverse('index'))
        else:
            return render(request, 'autentication/login.html', {'invalid_fields': True})