from django.contrib import admin

from .models import Complaint, ParecerDT


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

class ParecerDTAdmin(admin.ModelAdmin):
    """ definições do modelo de ParecerDT no Admin"""

    list_display = [
        'dt', 'complaint', 'parecer', 'created', 'modified',
    ]
    search_fields = [
        'dt', 'complaint', 'parecer', 'created', 'modified',
    ]
    list_filter = [
        'dt', 'complaint', 'parecer', 'created', 'modified',
    ]


admin.site.register(ParecerDT, ParecerDTAdmin)
