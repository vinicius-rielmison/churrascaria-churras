from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('finalizar/', views.finalizar, name='finalizar'),
    path('login_funcionario/', views.login_funcionario, name='login_funcionario'),
    path('Gerente/', views.Gerente, name='Gerente'),
    path('funcionario/', views.funcionario, name='funcionario'),

  
]