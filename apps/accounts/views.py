from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User


def login_view(request):
    ''' Login do utilizador na plataforma '''

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Efetuou login com sucesso, '{username}'")
                return redirect('home')
            else:
                messages.error(request, "Utilizador e/ou password inválidos!")
        else:
            messages.error(request, "Utilizador e/ou password inválidos!")
    form = AuthenticationForm()
    template_name = "accounts/login.html"
    context = {"form": form}
    return render(request, template_name, context)
