from django.conf.urls import url
from django.urls import path, reverse_lazy
from apps.game_features import views


app_name = 'game'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("participacao/criar/", views.complaint_add_view, name="complaint_add"),
]