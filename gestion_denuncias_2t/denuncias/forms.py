from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['titulo', 'descripcion', 'imagen', 'categoria']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }