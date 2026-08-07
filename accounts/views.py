from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg

from .forms import (
    RegistroForm,
    PerfilForm,
    VerificacionForm,
)

from .models import Usuario

from jobs.models import Calificacion, Propuesta


def registro(request):

    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():

            usuario = form.save()

            login(request, usuario)

            messages.success(
                request,
                "¡Tu cuenta fue creada correctamente!"
            )

            return redirect("completar_perfil")

    else:

        form = RegistroForm()

    return render(
        request,
        "accounts/registro.html",
        {
            "form": form,
        },
    )


@login_required
def completar_perfil(request):

    if request.method == "POST":

        form = PerfilForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            return redirect("verificar_identidad")

    else:

        form = PerfilForm(
            instance=request.user
        )

    return render(
        request,
        "accounts/completar_perfil.html",
        {
            "form": form,
        },
    )


@login_required
def verificar_identidad(request):

    if request.method == "POST":

        form = VerificacionForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Tus documentos fueron enviados correctamente. Un administrador revisará tu identidad."
            )

            return redirect("inicio")

    else:

        form = VerificacionForm(
            instance=request.user
        )

    return render(
        request,
        "accounts/verificar_identidad.html",
        {
            "form": form,
        },
    )


@login_required
def cerrar_sesion(request):

    logout(request)

    messages.info(
        request,
        "Has cerrado sesión correctamente."
    )

    return redirect("login")


def perfil(request, username):

    usuario = get_object_or_404(
        Usuario,
        username=username,
    )

    trabajos = usuario.trabajos.all()

    trabajos_realizados = Propuesta.objects.filter(
        trabajador=usuario,
        aceptada=True,
    ).count()

    calificaciones = Calificacion.objects.filter(
        trabajo__propuestas__trabajador=usuario,
        trabajo__propuestas__aceptada=True,
    ).distinct()

    promedio = calificaciones.aggregate(
        Avg("estrellas")
    )["estrellas__avg"]

    return render(
        request,
        "accounts/perfil.html",
        {
            "usuario": usuario,
            "trabajos": trabajos,
            "trabajos_realizados": trabajos_realizados,
            "calificaciones": calificaciones,
            "promedio": promedio,
        },
    )