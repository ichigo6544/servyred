from django import forms

from .models import Trabajo, Propuesta, Calificacion


class TrabajoForm(forms.ModelForm):

    class Meta:
        model = Trabajo

        fields = [
            "titulo",
            "descripcion",
            "ubicacion",
            "presupuesto",
            "horas_estimadas",
            "telefono_contacto",
            "imagen",
        ]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Título del trabajo",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe el trabajo...",
                }
            ),
            "ubicacion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ciudad o ubicación",
                }
            ),
            "presupuesto": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: 250000",
                }
            ),
            "horas_estimadas": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: 3",
                }
            ),
            "telefono_contacto": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "0981 123456",
                }
            ),
            "imagen": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class PropuestaForm(forms.ModelForm):

    class Meta:
        model = Propuesta

        fields = [
            "monto",
            "tiempo",
            "telefono",
            "mensaje",
        ]

        widgets = {
            "monto": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "¿Cuánto cobras?",
                }
            ),
            "tiempo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: 3 horas",
                }
            ),
            "telefono": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "0981 123456",
                }
            ),
            "mensaje": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Escribe tu propuesta...",
                }
            ),
        }


class CalificacionForm(forms.ModelForm):

    class Meta:
        model = Calificacion

        fields = [
            "estrellas",
            "comentario",
        ]

        widgets = {
            "estrellas": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "comentario": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Escribe tu opinión sobre el trabajo realizado...",
                }
            ),
        }