from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.pias.models import Pias

@login_required(login_url='/contas/login/')
def