from django.contrib import admin

from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    """ definições do modelo de participação disciplinar no Admin"""

    list_display = [
        'user', 'qualidade', 'aluno', 'ordem_saida', 'falta', 'created',
    ]
    search_fields = [
        'user', 'qualidade', 'aluno', 'ordem_saida', 'falta', 'created',
    ]
    list_filter = [
        'user', 'qualidade', 'aluno', 'ordem_saida', 'falta', 'created',
    ]


admin.site.register(Complaint, ComplaintAdmin)
