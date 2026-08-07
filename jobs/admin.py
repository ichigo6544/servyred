from django.contrib import admin

from .models import Trabajo, Propuesta, Calificacion


@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "usuario",
        "ubicacion",
        "presupuesto",
        "estado",
        "fecha_publicacion",
    )

    list_filter = (
        "estado",
        "fecha_publicacion",
    )

    search_fields = (
        "titulo",
        "descripcion",
        "ubicacion",
        "usuario__username",
    )


@admin.register(Propuesta)
class PropuestaAdmin(admin.ModelAdmin):

    list_display = (
        "trabajo",
        "trabajador",
        "monto",
        "aceptada",
        "fecha",
    )

    list_filter = (
        "aceptada",
        "fecha",
    )

    search_fields = (
        "trabajador__username",
        "trabajo__titulo",
    )


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):

    list_display = (
        "trabajo",
        "autor",
        "estrellas",
        "fecha",
    )

    list_filter = (
        "estrellas",
        "fecha",
    )

    search_fields = (
        "autor__username",
        "trabajo__titulo",
        "comentario",
    )