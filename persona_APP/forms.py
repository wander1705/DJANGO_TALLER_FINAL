from django import forms
from persona_APP.models import Proyecto

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'