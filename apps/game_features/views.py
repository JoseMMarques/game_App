from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.game_features.models import Complaint
from apps.accounts.models import User, Student
from .forms import ComplaintAddForm, ComplaintAddFormManual


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

    if request.method == 'POST':
        form = ComplaintAddFormManual(request.POST, participacao)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            participacao = form.save(commit=False)
            participacao.user_id = request.user.id
            participacao.class_number = request.POST.get('id_class_number', False)
            participacao.save()
            messages.success(request, f"Participação registada com sucesso")
            return redirect('game_features:homepage')
        else:
            if form.errors:
                for error in form.errors:
                    print(error)
                messages.error(request, "corrija os erros abaixo indicados")
            template_name = 'game_features/complaint_add.html'
            context = {'form': form}
            return render(request, template_name, context)

    form = ComplaintAddFormManual
    template_name = 'game_features/complaint_add.html'
    context = {'form': form}
    return render(request, template_name, context)


def load_alunos_da_turma(request):
    ''' carrega todos os alunos da turma selecionada no formulário
    da participação disciplinar '''

    try:
        name_id = request.GET.get('turma')
        print(request)
        alunos = Student.objects.filter(studentmore__school_class_id=name_id).order_by(('studentmore__class_number'))
        print(alunos)
        print("ok")
    except(ValueError, Student.DoesNotExist):
        alunos = Student.objects.none()
        print("BOA")

    template_name = 'game_features/alunos_dropdown_list_options.html'
    return render(
        request,
        template_name,
        {'alunos': alunos}
    )


def load_numero_do_aluno(request):
    ''' Carrega o número do aluno selecionado no formulário
    da participação disciplinar'''

    try:
        aluno_id = request.GET.get('aluno')
        print(request)
        objeto_aluno = Student.objects.get(id=aluno_id)
        print(objeto_aluno)
        numero_aluno = objeto_aluno.studentmore.class_number
        print(numero_aluno)
        print("ok Numero aluno")

    except(ValueError, Student.DoesNotExist):
        numero_aluno = None
        print("ok Numero aluno ERRO")

    template_name = 'game_features/numero_aluno.html'
    return render(
        request,
        template_name,
        {'numero_aluno': str(numero_aluno)}
    )
