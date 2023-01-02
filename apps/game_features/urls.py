from django.conf.urls import url
from django.urls import path, reverse_lazy
from apps.game_features import views


app_name = 'game'

urlpatterns = [
    path("", views.homepage, name="homepage"),
]