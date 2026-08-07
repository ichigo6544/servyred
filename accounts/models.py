from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):

    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    direccion = models.CharField(
        max_length=255,
        blank=True
    )

    foto = models.ImageField(
        upload_to="perfiles/",
        default="perfiles/default.png",
        blank=True
    )

    ci_frente = models.ImageField(
        upload_to="ci/",
        blank=True,
        null=True
    )

    ci_dorso = models.ImageField(
        upload_to="ci/",
        blank=True,
        null=True
    )
    selfie_ci = models.ImageField(
    upload_to="ci/",
    blank=True,
    null=True
)

    verificado = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.username