from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.game_features.models import Complaint
from .forms import ComplaintAddForm


@login_required(login_url='/contas/login/')
def homepage(request):

    template_name = 'game_features/homepage.html'
    context = {}
    return render(request, template_name, context)


@login_required
def complaint_add_view(request):
    ''' apresenta formulário para adição de uma participação '''

    participacao = Complaint()
    participacao.user = request.user
    form = ComplaintAddForm(request.POST or None, instance=participacao)
    if request.method == 'POST':
        if form.is_valid():
            participacao = form.save(commit=False)
            participacao.user_id = request.user.id
            participacao.save()
            messages.success(request, f"Participação registada com sucesso")
            return redirect('game_features:homepage')
        else:
            messages.error(request, "corrija os erros abaixo indicados")

    template_name = 'game_features/complaint_add.html'
    context = {'form': form}
    return render(request, template_name, context)
