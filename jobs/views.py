from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TrabajoForm, PropuestaForm, CalificacionForm
from .models import Trabajo, Propuesta, Calificacion


def inicio(request):

    trabajos = Trabajo.objects.all().order_by("-fecha_publicacion")

    buscar = request.GET.get("q")

    if buscar:

        trabajos = trabajos.filter(
            Q(titulo__icontains=buscar)
            | Q(descripcion__icontains=buscar)
            | Q(ubicacion__icontains=buscar)
        )

    return render(
        request,
        "jobs/lista.html",
        {
            "trabajos": trabajos,
        },
    )


@login_required
def crear_trabajo(request):

    if not request.user.verificado:

        messages.warning(
            request,
            "Debes verificar tu identidad antes de publicar trabajos."
        )

        return redirect("verificar_identidad")

    if request.method == "POST":

        form = TrabajoForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            trabajo = form.save(commit=False)

            trabajo.usuario = request.user

            trabajo.save()

            messages.success(
                request,
                "Trabajo publicado correctamente."
            )

            return redirect("inicio")

    else:

        form = TrabajoForm()

    return render(
        request,
        "jobs/crear.html",
        {
            "form": form,
        },
    )


@login_required
def detalle_trabajo(request, pk):

    trabajo = get_object_or_404(
        Trabajo,
        pk=pk,
    )

    if request.method == "POST":

        if not request.user.verificado:

            messages.warning(
                request,
                "Debes verificar tu identidad para enviar propuestas."
            )

            return redirect("verificar_identidad")

        form = PropuestaForm(request.POST)

        if form.is_valid():

            propuesta = form.save(commit=False)

            propuesta.trabajo = trabajo

            propuesta.trabajador = request.user

            propuesta.save()

            messages.success(
                request,
                "Propuesta enviada correctamente."
            )

            return redirect(
                "detalle_trabajo",
                pk=pk,
            )

    else:

        form = PropuestaForm()

    propuestas = trabajo.propuestas.all().order_by("-fecha")

    return render(
        request,
        "jobs/detalle.html",
        {
            "trabajo": trabajo,
            "form": form,
            "propuestas": propuestas,
        },
    )
@login_required
def editar_trabajo(request, pk):

    trabajo = get_object_or_404(
        Trabajo,
        pk=pk,
        usuario=request.user,
    )

    if request.method == "POST":

        form = TrabajoForm(
            request.POST,
            request.FILES,
            instance=trabajo,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Trabajo actualizado correctamente."
            )

            return redirect(
                "detalle_trabajo",
                pk=pk,
            )

    else:

        form = TrabajoForm(
            instance=trabajo,
        )

    return render(
        request,
        "jobs/editar.html",
        {
            "form": form,
        },
    )


@login_required
def eliminar_trabajo(request, pk):

    trabajo = get_object_or_404(
        Trabajo,
        pk=pk,
        usuario=request.user,
    )

    if request.method == "POST":

        trabajo.delete()

        messages.success(
            request,
            "Trabajo eliminado correctamente."
        )

        return redirect("inicio")

    return render(
        request,
        "jobs/eliminar.html",
        {
            "trabajo": trabajo,
        },
    )


@login_required
def aceptar_propuesta(request, propuesta_id):

    if not request.user.verificado:

        messages.warning(
            request,
            "Debes verificar tu identidad antes de aceptar propuestas."
        )

        return redirect("verificar_identidad")

    propuesta = get_object_or_404(
        Propuesta,
        id=propuesta_id,
    )

    trabajo = propuesta.trabajo

    if trabajo.usuario != request.user:

        return redirect(
            "detalle_trabajo",
            pk=trabajo.id,
        )

    Propuesta.objects.filter(
        trabajo=trabajo,
    ).update(
        aceptada=False,
    )

    propuesta.aceptada = True

    propuesta.save()

    trabajo.estado = "ACEPTADO"

    trabajo.save()

    messages.success(
        request,
        "Has aceptado la propuesta correctamente."
    )

    return redirect(
        "detalle_trabajo",
        pk=trabajo.id,
    )
@login_required
def finalizar_trabajo(request, pk):

    trabajo = get_object_or_404(
        Trabajo,
        pk=pk,
    )

    if trabajo.usuario != request.user:

        return redirect(
            "detalle_trabajo",
            pk=pk,
        )

    trabajo.estado = "FINALIZADO"

    trabajo.save()

    messages.success(
        request,
        "El trabajo fue marcado como finalizado."
    )

    return redirect(
        "detalle_trabajo",
        pk=pk,
    )


@login_required
def calificar_trabajo(request, pk):

    trabajo = get_object_or_404(
        Trabajo,
        pk=pk,
    )

    if trabajo.usuario != request.user:

        return redirect(
            "detalle_trabajo",
            pk=pk,
        )

    if trabajo.estado != "FINALIZADO":

        return redirect(
            "detalle_trabajo",
            pk=pk,
        )

    if Calificacion.objects.filter(
        trabajo=trabajo,
        autor=request.user,
    ).exists():

        messages.info(
            request,
            "Ya calificaste este trabajo."
        )

        return redirect(
            "detalle_trabajo",
            pk=pk,
        )

    propuesta = trabajo.propuestas.filter(
        aceptada=True,
    ).first()

    if propuesta is None:

        return redirect(
            "detalle_trabajo",
            pk=pk,
        )

    if request.method == "POST":

        form = CalificacionForm(request.POST)

        if form.is_valid():

            calificacion = form.save(commit=False)

            calificacion.trabajo = trabajo

            calificacion.autor = request.user

            calificacion.save()

            messages.success(
                request,
                "Gracias por tu calificación."
            )

            return redirect(
                "detalle_trabajo",
                pk=pk,
            )

    else:

        form = CalificacionForm()

    return render(
        request,
        "jobs/calificar.html",
        {
            "trabajo": trabajo,
            "trabajador": propuesta.trabajador,
            "form": form,
        },
    )
def politicas(request):

    return render(
        request,
        "jobs/politicas.html",
    )