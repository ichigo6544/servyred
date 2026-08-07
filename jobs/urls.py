from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.inicio,
        name="inicio",
    ),

    path(
        "trabajo/nuevo/",
        views.crear_trabajo,
        name="crear_trabajo",
    ),

    path(
        "trabajo/<int:pk>/",
        views.detalle_trabajo,
        name="detalle_trabajo",
    ),

    path(
        "trabajo/<int:pk>/editar/",
        views.editar_trabajo,
        name="editar_trabajo",
    ),

    path(
        "trabajo/<int:pk>/eliminar/",
        views.eliminar_trabajo,
        name="eliminar_trabajo",
    ),

    path(
        "trabajo/<int:pk>/finalizar/",
        views.finalizar_trabajo,
        name="finalizar_trabajo",
    ),

    path(
        "trabajo/<int:pk>/calificar/",
        views.calificar_trabajo,
        name="calificar_trabajo",
    ),

    path(
        "propuesta/<int:propuesta_id>/aceptar/",
        views.aceptar_propuesta,
        name="aceptar_propuesta",
    ),
    path(
    "politicas/",
    views.politicas,
    name="politicas",
),
]
