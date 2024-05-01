from django import forms
from . import models

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'surname': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'user': forms.Select(choices=models.User.objects.all(), attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'})
        }