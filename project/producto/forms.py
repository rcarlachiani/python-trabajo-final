from django import forms
from . import models

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = models.Categorias
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'category': forms.Select(choices=models.Categorias.objects.all(), attrs={'class': 'form-control mb-3'})
        }
