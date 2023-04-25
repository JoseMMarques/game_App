from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from apps.accounts.models import User, Student, Teacher
from apps.school_structure.models import SchoolClass


class Complaint(models.Model):
    """ Um modelo para as participações disciplinares """

    # identificação
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    QUALIDADE_CHOICES = (
        ('A', 'Aluno'),
        ('F', 'Funcionário'),
        ('P', 'Professor'),
    )
    qualidade = models.CharField(
        'qualidade',
        choices=QUALIDADE_CHOICES,
        max_length=100,
        default='P',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        help_text="Deixar em branco para criar um slug automático e único",
    )

    turma = models.ForeignKey(
        SchoolClass,
        related_name='turma',
        on_delete=models.CASCADE
    )
    dt = models.ForeignKey(
        Teacher,
        related_name='DT',
        on_delete=models.CASCADE
    )

    class_number = models.CharField(
        "Número",
        max_length=200,
    )
    aluno = models.ForeignKey(
        Student,
        related_name='aluno',
        on_delete=models.CASCADE
    )
    local = models.CharField(
        "Local da ocorrência",
        max_length=200,
    )
    hora = models.TimeField(
        "Hora da ocorrência",
    )
    dia = models.DateField(
        'Dia da ocorrência',
    )

    # comportamentos incorretos
    comer = models.BooleanField(
        'Comer na sala de aula.',
        default=False,
    )
    levantar = models.BooleanField(
        'Levantar-se durante a aula sem autorização.',
        default=False,
    )
    conversar = models.BooleanField(
        'Perturbar a aula com conversa e brincadeira.',
        default=False,
    )
    entradar_sair_desordeira = models.BooleanField(
        'Entrar/sair da aula de forma desordeira.',
        default=False,
    )
    patrimonio = models.BooleanField(
        'Não respeitar o património escolar.',
        default=False,
    )
    recolher_imagens = models.BooleanField(
        'Recolher/divulgar imagens/sons sem autorização.',
        default=False,
    )
    fumar = models.BooleanField(
        'Fumar dentro do recinto escolar.',
        default=False,
    )
    regras_espaços = models.BooleanField(
        'Não cumprir as regras de utilização dos diversos espaços.',
        default=False,
    )
    aparelhos_eletronicos = models.BooleanField(
        'Utilizar indevidamente o telemóvel ou outro aparelho eletrónico.',
        default=False,
    )
    linguagem = models.BooleanField(
        'Utilizar linguagem imprópria.',
        default=False,
    )
    ofender_colegas = models.BooleanField(
        'Ofender verbalmente os colegas.',
        default=False,
    )
    ameacar = models.BooleanField(
        'Ameaçar/intimidar colegas.',
        default=False,
    )
    recusar_trabalhar = models.BooleanField(
        'Recusar-se a trabalhar.',
        default=False,
    )
    abandonar_aula = models.BooleanField(
        'Abandonar a aula sem autorização do professor.',
        default=False,
    )
    Ofender_prof_fun = models.BooleanField(
        'Ofender verbalmente professores/funcionários.',
        default=False,
    )
    roubar = models.BooleanField(
        'Roubar/furtar.',
        default=False,
    )
    nao_obedecer = models.BooleanField(
        'Não obedecer às indicações do adulto.',
        default=False,
    )
    agredir = models.BooleanField(
        'Agredir.',
        default=False,
    )
    contextualizacao = models.TextField(
        'Breve descrição/contextualização do(s) comportamento(s) incorreto(s):',
        blank=True,
    )

    # campos de informação complementar
    ATIVIDADE_CHOICES = (
        ('EM', 'em atividade letiva'),
        ('FORA', 'fora de atividade letiva'),
    )
    atividade = models.CharField(
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
    ESTADO_CHOICES = (
        ('ANALISE', 'Em análise'),
        ('ARQUIVADA', 'Arquivada'),
        ('CONCLUIDA', 'Participação disciplinar registada'),
        ('PROCEDIMENTO', 'Procedimento Disciplinar Sumário'),
        ('EMD', 'Procedimento Disciplinar - EMD'),
    )
    estado = models.CharField(
        'Estado',
        choices=ESTADO_CHOICES,
        max_length=100,
        default='ANALISE',
    )
    parecer_dt = models.BooleanField(
        'Participação com parecer do DT',
        default=False,
    )
    created = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now=True
    )

    class Meta:
        """options (metadata) to the field"""
        verbose_name = "Participação disciplinar"
        verbose_name_plural = "Participações disciplinares"
        ordering = ['user']

    def __str__(self):
        """Return the str.name fom the object"""
        return self.user.name

    def get_absolute_url(self):
        return reverse(
            'game_features:complaint_detail',
            kwargs={'participacao_slug': self.slug}
        )

    def save(self, *args, **kwargs):
        """ Set automatic and unique slug from turma, numero e id filed"""
        super(Complaint, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.turma) + str(self.class_number) + "_" + str(self.id)
            self.save()

# fazer drop nesta tabela
# https://stackoverflow.com/questions/54256136/how-to-drop-a-table-sqlite3-in-django-2-1

# corrigir erros da tabela --- ver este link -> answered Feb 17, 2020 at 20:49
# Ashish Gupta
# https://stackoverflow.com/questions/34548768/no-such-table-exception

# procedimento
# 1 - abrir o executavel "sqlite3.exe" na pasta do projeto
# 2 - correr o comando para abrir a base de dados
#     .open db.sqlite3
# 3 - ver tabelas
#     .table
# 4 - apagar esta tabela
#     DROP TABLE game_features_complaint;
# 5 - apagar migrações da app
# 6 - correr python manage.py makemigrations
# 7 - Follow this steps to get fixed this issue.
#
# python manage.py migrate --fake APPNAME zero
# This will make your migration to fake. Now you can run the migrate script
#
# python manage.py migrate APPNAME
# OR
# python manage.py migrate
# Tables will be created and you solved your problem.. Cheers!!!


class ParecerDT(models.Model):
    """ Um modelo para as ações dos DTs nas participações disciplinares """

    # identificação

    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        help_text="Deixar em branco para criar um slug automático e único",
    )
    dt = models.ForeignKey(
        Teacher,
        related_name='DiretorTurma',
        on_delete=models.CASCADE
    )
    complaint = models.ForeignKey(
        Complaint,
        related_name='participacao',
        on_delete=models.CASCADE
    )

    PARECER_CHOICES = (
        ('1', 'Participação arquivada e sem efeito.'),
        ('2', 'Ocorrência não frequente e não grave.'),
        ('3', 'Procedimento disciplinar sumário.'),
        ('4', 'Procedimento disciplinar sumário - Equipa EMD.'),
    )
    parecer = models.CharField(
        'Parecer do DT',
        choices=PARECER_CHOICES,
        max_length=250,
        default='F',
    )

    # ações DT
    advertencia_verbal_aluno = models.BooleanField(
        'Advertência verbal ao aluno.',
        default=False,
    )
    comunicacao_EE = models.BooleanField(
        'Comunicação ao Encarregado de Educação.',
        default=False,
    )
    descricao_acao_dt = models.TextField(
        'Breve descrição da(s) ações(s) tomadas(s) pelo DT:',
        blank=True,
    )
    created = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now=True
    )

    class Meta:
        """options (metadata) to the field"""
        verbose_name = "Parecer do DT"
        verbose_name_plural = "Pareceres dos DT's"
        ordering = ['created']

    def __str__(self):
        """Return the str.name fom the object"""
        return self.dt.name

    def save(self, *args, **kwargs):
        """ Set automatic and unique slug from turma, numero e id filed"""
        super(ParecerDT, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.complaint.slug) + "-" + str(self.id)
            self.save()
