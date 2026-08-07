from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class RegistroForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Correo electrónico",
            }
        ),
    )

    class Meta:

        model = Usuario

        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

        widgets = {

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Apellido",
                }
            ),

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Usuario",
                }
            ),

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Contraseña",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Confirmar contraseña",
            }
        )


class PerfilForm(forms.ModelForm):

    class Meta:

        model = Usuario

        fields = (
            "foto",
            "telefono",
            "direccion",
        )

        widgets = {

            "foto": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                    "capture": "environment",
                }
            ),

            "telefono": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Teléfono",
                }
            ),

            "direccion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Dirección",
                }
            ),

        }


class VerificacionForm(forms.ModelForm):

    class Meta:

        model = Usuario

        fields = (
            "ci_frente",
            "ci_dorso",
            "selfie_ci",
        )

        widgets = {

            "ci_frente": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                    "capture": "environment",
                }
            ),

            "ci_dorso": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                    "capture": "environment",
                }
            ),

            "selfie_ci": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                    "capture": "user",
                }
            ),

        }