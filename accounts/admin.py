from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "telefono",
        "verificado",
        "is_staff",
    )

    list_filter = (
        "verificado",
        "is_staff",
        "is_superuser",
        "is_active",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Información de ServiRed",
            {
                "fields": (
                    "telefono",
                    "direccion",
                    "foto",
                    "ci_frente",
                    "ci_dorso",
                    "selfie_ci",
                    "verificado",
                ),
            },
        ),
    )