from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse


# Create your views here.
def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuáro {usuario} foi criado com sucesso!')
            return redirect('login')
    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html',{'formulario': formulario})

class CustomLogoutView(LogoutView):
    next_page = 'usuarios/logout.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return super().dispatch(request, *args, **kwargs)
        else:
            return super().dispatch(request, *args, **kwargs)