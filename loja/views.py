from django.shortcuts import render


def inicio(request): 
    return render(request, 'loja/loja.html') 

def finalizar(request):
    return render(request, 'loja/finalizar.html')

def login_funcionario(request):
    return render(request, 'loja/login_funcionario.html')

def Gerente(request):
    return render(request, 'loja/login_funcionario.html')

def funcionario(request):
    return render(request, 'loja/funcionario.html')



