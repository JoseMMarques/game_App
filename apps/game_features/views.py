from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.game_features.models import Complaint
from apps.accounts.models import User, Student, Teacher
from .forms import ComplaintAddFormManual


@login_required(login_url='/contas/login/')
def homepage(request):
    template_name = 'game_features/homepage.html'
    context = {}
    user = User.objects.get(id=request.user.id)
    print('request user')
    print(user)

    # as minhas participações disciplinares
    my_complaits = Complaint.objects.filter(user=user).order_by('-created')
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
                my_dt_complaints = Complaint.objects.filter(turma=turma).order_by('-created')
                context['my_dt_complaints'] = my_dt_complaints
                print('ProfDT')
                print(context['my_dt_complaints'])
        except:
            print('o professor não é DT')

    # Se user for do GAME
    # listar participações de todos os alunos da escola  :)
    if user.is_game:
        all_complaints = Complaint.objects.all().order_by('-created')
        context['all_complaints'] = all_complaints
        print('MembroGame')
        print(context['all_complaints'])

    return render(request, template_name, context)


@login_required
def complaint_add_view(request):
    """ apresenta formulário para adição de uma participação """

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
            participacao.dt = Teacher.objects.get(teachermore__school_class_dt=data['turma'])
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
    """ carrega todos os alunos da turma selecionada no formulário
    da participação disciplinar """

    try:
        name_id = request.GET.get('turma')
        print(request)
        alunos = Student.objects.filter(studentmore__school_class_id=name_id).order_by('studentmore__class_number')
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
    """ Carrega o número do aluno selecionado no formulário
    da participação disciplinar"""

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


def complaint_detail_view(request, participacao_slug):
    """ apresenta informação detalhada de uma participação """

    complaint = get_object_or_404(Complaint, slug=participacao_slug)

    teste = complaint._meta.get_field('comer').verbose_name
    # print(teste)

    # dicionário com o verbose_name dos campos do modelo complaint
    complaint_vb = {
        'comer': complaint._meta.get_field('comer').verbose_name,
        'levantar': complaint._meta.get_field('levantar').verbose_name,
        'conversar': complaint._meta.get_field('conversar').verbose_name,
        'entradar_sair_desordeira': complaint._meta.get_field('entradar_sair_desordeira').verbose_name,
        'patrimonio': complaint._meta.get_field('patrimonio').verbose_name,
        'recolher_imagens': complaint._meta.get_field('recolher_imagens').verbose_name,
        'fumar': complaint._meta.get_field('fumar').verbose_name,
        'regras_espaços': complaint._meta.get_field('regras_espaços').verbose_name,
        'aparelhos_eletronicos': complaint._meta.get_field('aparelhos_eletronicos').verbose_name,
        'linguagem': complaint._meta.get_field('linguagem').verbose_name,
        'ofender_colegas': complaint._meta.get_field('ofender_colegas').verbose_name,
        'ameacar': complaint._meta.get_field('ameacar').verbose_name,
        'recusar_trabalhar': complaint._meta.get_field('recusar_trabalhar').verbose_name,
        'abandonar_aula': complaint._meta.get_field('abandonar_aula').verbose_name,
        'Ofender_prof_fun': complaint._meta.get_field('Ofender_prof_fun').verbose_name,
        'roubar': complaint._meta.get_field('roubar').verbose_name,
        'nao_obedecer': complaint._meta.get_field('nao_obedecer').verbose_name,
        'agredir': complaint._meta.get_field('agredir').verbose_name,
        'ordem_saida': complaint._meta.get_field('ordem_saida').verbose_name,
        'falta': complaint._meta.get_field('falta').verbose_name,
    }

    template_name = 'game_features/complaint_detail.html'
    context = {
        'complaint': complaint,
        'complaint_vb': complaint_vb,
    }

    return render(request, template_name, context)


def complaints_aluno_view(request, aluno_id):
    """ apresenta lista de todas as participações de um aluno """

    aluno = get_object_or_404(Student, id=aluno_id)
    print(aluno.type)

    participacoes = Complaint.objects.filter(aluno_id=aluno.id)
    print(participacoes)

    template_name = 'game_features/complaints_aluno_list.html'
    context = {
        'aluno': aluno,
        'participacoes': participacoes,
    }

    return render(request, template_name, context)

