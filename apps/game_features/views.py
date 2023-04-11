from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.game_features.models import Complaint
from apps.accounts.models import User, Student, Teacher
from .forms import ComplaintAddForm, ComplaintAddFormManual


@login_required(login_url='/contas/login/')
def homepage(request):

    template_name = 'game_features/homepage.html'
    context = {}
    user = User.objects.get(id=request.user.id)
    print('request user')
    print(user)

    # as minhas participações disciplinares
    my_complaits = Complaint.objects.filter(user=user)
    context['my_complaints'] = my_complaits
    print('Base')
    print(context)

    # Se diretor turma
    # lista com participações da minha direcao de turma
    if user.type == user.Types.TEACHER:
        teacher = Teacher.objects.get(id=user.id)
        print('teacher')
        print(teacher)
        try:
            # para o caso do professor não ter dados na classe TeacherMore
            if teacher.teachermore.is_dt:
                turma = teacher.teachermore.school_class_dt
                print(turma)
                my_dt_complaints = Complaint.objects.filter(aluno__studentmore__school_class=turma)
                context['my_dt_complaints'] = my_dt_complaints
                print('ProfDT')
                print(context['my_dt_complaints'])
        except:
            print('o professor não é DT')

    # Se user for do GAME
    # listar participações de todos os alunos da escola  :)
    if user.is_game:
        all_complaints = Complaint.objects.all()
        context['all_complaints'] = all_complaints
        print('MembroGame')
        print(context['all_complaints'])


    return render(request, template_name, context)


@login_required
def complaint_add_view(request):
    ''' apresenta formulário para adição de uma participação '''

    participacao = Complaint()
    participacao.user = request.user
    user = User.objects.get(id=request.user.id)

    # para inserir o tipo de utilizador (qualidade) no formulário de participação
    qualidade = ''
    print(user.type)
    if user.type == user.Types.EMPLOYEE:
        qualidade = 'F'
    if user.type == user.Types.STUDENT:
        qualidade = 'A'
    if user.type == user.Types.TEACHER:
        qualidade = 'P'

    if request.method == 'POST':
        form = ComplaintAddFormManual(request.POST, participacao)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            participacao = form.save(commit=False)
            participacao.user_id = request.user.id
            participacao.class_number = int(data['class_number'])
            participacao.qualidade = qualidade
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
        {'numero_aluno': numero_aluno}
    )
