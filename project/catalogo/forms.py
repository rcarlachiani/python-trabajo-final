from django import forms
from . import models

class FormatForm(forms.ModelForm):
    class Meta:
        model = models.Format
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'format': forms.Select(choices=models.Format.objects.all(), attrs={'class': 'form-control'}),
            'genre': forms.Select(choices=models.Genre.objects.all(), attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['format'].empty_label = 'Seleccione un formato'
        self.fields['genre'].empty_label = 'Seleccione un género'
