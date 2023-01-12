from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/contas/login/')
def homepage(request):

    template_name = 'game_features/homepage.html'
    context = {}
    return render(request, template_name, context)
