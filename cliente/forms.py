from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['apepaterno', 'apematerno', 'nombre', 'domicilio', 'correo_electronico', 'telefono', 'alergias']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar clases CSS a todos los campos
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})