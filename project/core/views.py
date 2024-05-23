from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView

def home(request):
  return render(request, 'core/index.html')

def about(request):
  return render(request, 'core/about.html')

class CustomLoginView(LoginView):
  autentication_form = CustomAuthenticationForm
  template_name = 'core/login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})