from django.conf.urls import url
from django.urls import path, reverse_lazy
from apps.accounts import views

# utilizado para envio de emails de recuperação de senha
from django.contrib.auth import views as auth_views

app_name = 'contas'

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # change password
    path("change_password/", views.change_password, name="change_password"),

    # reset password with email

]
