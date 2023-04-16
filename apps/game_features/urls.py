from django.conf.urls import url
from django.urls import path, reverse_lazy
from apps.game_features import views


app_name = 'game_features'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("participacao/criar/", views.complaint_add_view, name="complaint_add"),
    path("participacao/detalhe/<participacao_slug>", views.complaint_detail_view, name="complaint_detail"),
    path("participacao/detalhe/aluno/<aluno_id>", views.complaints_aluno_view, name="complaints_aluno"),
    path("ajax/load-alunos/", views.load_alunos_da_turma, name="ajax_load_alunos"),
    path("ajax/load-numero-aluno/", views.load_numero_do_aluno, name="ajax_load_numero_aluno"),
]

