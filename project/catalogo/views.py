from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from . import models, forms

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('core:home')

def home(request):
    consulta = request.GET.get('consulta')
    if consulta:
        productos = models.Product.objects.filter(name__icontains=consulta)
    else:
        productos = models.Product.objects.all()
    context = {
        'productos': productos,
        'consulta_actual': consulta
    }
    if 'limpiar' in request.GET:  
        return redirect('catalogo:home')
    return render(request, 'catalogo/index.html', context)

class FormatCreate(LoginRequiredMixin, StaffRequiredMixin, CreateView):
  model = models.Format
  form_class = forms.FormatForm
  success_url = reverse_lazy('catalogo:home')

class GenreCreate(LoginRequiredMixin, StaffRequiredMixin, CreateView):
  model = models.Genre
  form_class = forms.GenreForm
  success_url = reverse_lazy('catalogo:home')

class ProductCreate(LoginRequiredMixin, StaffRequiredMixin, CreateView):
  model = models.Product
  form_class = forms.ProductForm
  success_url = reverse_lazy('catalogo:home')
  def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.image = self.request.FILES.get('image')
        self.object.save()
        return super().form_valid(form)

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('catalogo:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if 'image' in self.request.FILES:
            self.object.image = self.request.FILES['image']
        else:
            previous_instance = models.Product.objects.get(pk=self.object.pk)
            self.object.image = previous_instance.image
        self.object.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
  model = models.Product
  context_object_name = 'producto'

class ProductDelete(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
  model = models.Product
  success_url = reverse_lazy('catalogo:home')