from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template_name = 'game_app_main/home.html'
    message = 'Gabinete de Apoio e Mediação Escolar'
    context = {'msn': message}
    return render(request, template_name, context)
