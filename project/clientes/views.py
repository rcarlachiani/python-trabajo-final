from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DetailView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from core.forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login
from . import models

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('clientes:home')

def not_staff(user):
    return user.is_staff

@login_required
@user_passes_test(not_staff)
def home(request):
    consulta = request.GET.get('consulta')
    if consulta:
        clientes = User.objects.filter(
            Q(first_name__icontains=consulta) | Q(last_name__icontains=consulta),
            is_staff=False
        )
    else:
        clientes = User.objects.filter(is_staff=False)
    context = {
        'clientes': clientes,
        'consulta_actual': consulta
    }
    if 'limpiar' in request.GET:
        return redirect('clientes:home')
    return render(request, 'clientes/index.html', context)

class ClienteDetail(LoginRequiredMixin, StaffRequiredMixin, DetailView):
  model = models.Client
  context_object_name = 'cliente'

class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'clientes/client_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        new_password = form.cleaned_data.get('password')
        if new_password:
            user.set_password(new_password)
        user.save()

        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        update_session_auth_hash(self.request, user) 

        return super().form_valid(form)
    
    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('clientes:home')
        else:
            return reverse_lazy('core:home')