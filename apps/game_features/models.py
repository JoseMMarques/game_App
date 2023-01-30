from django.db import models
from apps.accounts.models import User, Student, Teacher


class Complaint(models.Model):
    ''' Um modelo para as participações disciplinares '''

    # identificação
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    aluno = models.ForeignKey(
        Student,
        related_name='aluno',
        on_delete=models.CASCADE
    )
    hora = models.TimeField(
        "hora",
    )
    dia = models.DateField(
        'dia',
    )

    # comportamentos incorretos
    comer = models.BooleanField(
        'Comer na sala de aula',
        default=False,
    )
    levantar = models.BooleanField(
        'Levantar-se durante a aula sem autorização',
        default=False,
    )
    conversar = models.BooleanField(
        'Perturbar a aula com conversa e brincadeira',
        default=False,
    )
    entradar_sair_desordeira = models.BooleanField(
        'Entrar/sair da aula de forma desordeira',
        default=False,
    )
    patrimonio = models.BooleanField(
        'Não respeitar o património escolar',
        default=False,
    )
    recolher_imagens = models.BooleanField(
        'Recolher/divulgar imagens/sons sem autorização',
        default=False,
    )
    fumar = models.BooleanField(
        'Fumar dentro do recinto escolar',
        default=False,
    )
    regras_espaços = models.BooleanField(
        'Não cumprir as regras de utilização dos diversos espaços',
        default=False,
    )
    aparelhos_eletronicos = models.BooleanField(
        'Utilizar indevidamente o telemóvel ou outro aparelho eletrónico',
        default=False,
    )
    linguagem = models.BooleanField(
        'Utilizar linguagem imprópria',
        default=False,
    )
    Ofender_colegas = models.BooleanField(
        'Ofender verbalmente os colegas',
        default=False,
    )
    ameacar = models.BooleanField(
        'Ameaçar/intimidar colegas',
        default=False,
    )
    recusar_trabalhar = models.BooleanField(
        'recusar-se a trabalhar',
        default=False,
    )
    abandonar_aula = models.BooleanField(
        'abandonar a aula sem autorização do professor',
        default=False,
    )
    Ofender_prof_fun = models.BooleanField(
        'Ofender verbalmente professores/funcionários',
        default=False,
    )
    roubar = models.BooleanField(
        'Roubar/furtar',
        default=False,
    )
    nao_obedecer = models.BooleanField(
        'Não obedecer às indicações do adulto',
        default=False,
    )
    agredir = models.BooleanField(
        'Agredir',
        default=False,
    )
    contextualizacao = models.TextField(
        'Breve descrição/contextualização do comportamento incorreto do aluno',
        blank=True,
    )

    # campos de informação complementar
    ATIVIDADE_CHOICES = (
        ('EM', 'em atividade Letiva'),
        ('FORA', 'fora de atividade letiva'),
    )
    sex = models.CharField(
        'Tipo de atividade',
        choices=ATIVIDADE_CHOICES,
        max_length=50,
        default='EM',
    )
    ordem_saida = models.BooleanField(
        'Dada ordem de saída da sala de aula',
        default=False,
    )
    falta = models.BooleanField(
        'Marcada falta',
        default=False,
    )
    tarefa = models.TextField(
        'Encaminhamento com a tarefa:',
        blank=True,
    )
    created = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )

    # TODO: fazer formulário para este modelo
