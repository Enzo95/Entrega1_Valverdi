from django import forms

class AltaSocioForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    n_socio = forms.IntegerField()
    fecha_ingreso = forms.DateField()
    email = forms.EmailField()