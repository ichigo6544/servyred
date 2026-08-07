from django.db import models
from django.conf import settings


class Trabajo(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=100)

    presupuesto = models.DecimalField(
    max_digits=12,
    decimal_places=2
     ) 

    horas_estimadas = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    telefono_contacto = models.CharField(
        max_length=20,
        blank=True
    )

    imagen = models.ImageField(
        upload_to="trabajos/",
        blank=True,
        null=True
    )

    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="trabajos"
    )

    estado = models.CharField(
        max_length=20,
        choices=[
            ("DISPONIBLE", "Disponible"),
            ("ACEPTADO", "Aceptado"),
            ("FINALIZADO", "Finalizado"),
        ],
        default="DISPONIBLE"
    )

    def __str__(self):
        return self.titulo


class Propuesta(models.Model):
    trabajo = models.ForeignKey(
        Trabajo,
        on_delete=models.CASCADE,
        related_name="propuestas"
    )

    trabajador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    monto = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    tiempo = models.CharField(
        max_length=100
    )

    telefono = models.CharField(
        max_length=20
    )

    mensaje = models.TextField()

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    aceptada = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.trabajador.username} - {self.trabajo.titulo}"


class Calificacion(models.Model):
    trabajo = models.ForeignKey(
        Trabajo,
        on_delete=models.CASCADE,
        related_name="calificaciones"
    )

    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="calificaciones_realizadas"
    )

    estrellas = models.PositiveSmallIntegerField(
        choices=[
            (1, "⭐"),
            (2, "⭐⭐"),
            (3, "⭐⭐⭐"),
            (4, "⭐⭐⭐⭐"),
            (5, "⭐⭐⭐⭐⭐"),
        ]
    )

    comentario = models.TextField()

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.autor.username} - {self.estrellas}★"