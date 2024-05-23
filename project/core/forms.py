from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from clientes.models import Client

class CustomAuthenticationForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(label='Teléfono', required=False)
    birthdate = forms.DateField(label='Fecha de nacimiento', required=False)
    avatar = forms.ImageField(label='Avatar', required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'birthdate', 'avatar']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone = self.cleaned_data['phone']
        user.birthdate = self.cleaned_data['birthdate']
        if 'avatar' in self.cleaned_data:
            user.avatar = self.cleaned_data['avatar']  # Guardar el avatar solo si está presente en los datos limpios
        if commit:
            user.save()
            client = Client.objects.create(user=user, phone=self.cleaned_data['phone'], 
                                             birthdate=self.cleaned_data['birthdate'], 
                                             avatar=user.avatar)  # Usar user.avatar aquí
        return user
  
class CustomUserChangeForm(forms.ModelForm):
    phone = forms.CharField(label='Teléfono', required=False)
    birthdate = forms.DateField(label='Fecha de nacimiento', required=False)
    avatar = forms.ImageField(label='Avatar', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'phone', 'birthdate', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            client = self.instance.client
            self.initial['phone'] = client.phone
            self.initial['birthdate'] = client.birthdate
            self.initial['avatar'] = client.avatar
        except Client.DoesNotExist:
            pass 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone = self.cleaned_data['phone']
        user.birthdate = self.cleaned_data['birthdate']
        user.avatar = self.cleaned_data['avatar']
        
        if commit:
            user.save()
            try:
                client = user.client
                client.phone = self.cleaned_data['phone']
                client.birthdate = self.cleaned_data['birthdate']
                client.avatar = self.cleaned_data['avatar']
                client.save()
            except Client.DoesNotExist:
                pass
        return user