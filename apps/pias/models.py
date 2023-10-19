from django.db import models


class Pias(models.Model):
    """Um modelo para os PIAS dos alunos"""

    student_name = models.CharField(
        'Nome do aluno',
        max_length=254,
    )
    process_number = models.IntegerField(
        'Número de processo',
        unique=True,
    )

    TYPE_OPTIONS = (
        ("relatorio", "Relatório"),
        ("ficha_informativa", "Ficha Informativa"),
        ("procedimento_disciplinar", "Procedimento Disciplinar"),
        ("participacao_disciplinar", "Participação Disciplinar"),
        ("certidao", "Certidão"),
        ("registo_avaliacao", "Registo Avaliação"),
        ("outro", "Outro"),
    )

    type = models.CharField(
        "Tipo de documento",
        choices=TYPE_OPTIONS,
        default='Outro',
    )

    description = models.TextField(
        'Descrição do documento:',
        blank=True,
    )