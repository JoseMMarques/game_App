from django.contrib import admin

from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    """ definições do modelo de participação disciplinar no Admin"""

    list_display = [
        'user', 'qualidade', 'turma', 'class_number', 'aluno', 'created', 'estado',
    ]
    search_fields = [
        'user', 'qualidade', 'turma', 'class_number', 'aluno', 'created', 'estado',
    ]
    list_filter = [
        'user', 'qualidade', 'turma', 'class_number', 'aluno', 'created', 'estado',
    ]


admin.site.register(Complaint, ComplaintAdmin)
