from django import forms

class IngresarForm(forms.Form):
    cad = forms.CharField(label='cadena', max_length=2000)
    email = forms.EmailField()
    nom = forms.CharField(label='name', max_length=250)

class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email