from django import forms

class IngresarForm(forms.Form):
    cad = forms.CharField(label='cadena', max_length=2000)
    email = forms.EmailField()
    nom = forms.CharField(label='name', max_length=250)