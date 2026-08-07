from django.urls import path
from django.contrib.auth.views import LoginView

from . import views


urlpatterns = [

    path(
        "registro/",
        views.registro,
        name="registro",
    ),

    path(
        "login/",
        LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        views.cerrar_sesion,
        name="logout",
    ),

    path(
        "perfil/<str:username>/",
        views.perfil,
        name="perfil",
    ),

    path(
        "completar-perfil/",
        views.completar_perfil,
        name="completar_perfil",
    ),

    path(
        "verificar-identidad/",
        views.verificar_identidad,
        name="verificar_identidad",
    ),

]