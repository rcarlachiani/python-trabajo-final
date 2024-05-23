from django import forms
from . import models

class FormatForm(forms.ModelForm):
    class Meta:
        model = models.Format
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'}),
            'price': forms.TextInput(attrs={
                'class': 'form-control mb-2', 
                'placeholder': 'Precio', 
                'inputmode': 'numeric', 
            }),
            'format': forms.Select(choices=models.Format.objects.all(), attrs={'class': 'form-control mb-2'}),
            'genre': forms.Select(choices=models.Genre.objects.all(), attrs={'class': 'form-control mb-2'}),
            'stock': forms.TextInput(attrs={
                'class': 'form-control mb-2', 
                'placeholder': 'Stock', 
                'inputmode': 'numeric', 
            }),
            'image': forms.FileInput(attrs={'class': 'form-control mb-2'})
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['format'].empty_label = 'Seleccione un formato'
        self.fields['genre'].empty_label = 'Seleccione un género'
