from django import forms
from .models import Libro

#  se crea el formulario con los campos del modelo libro
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'