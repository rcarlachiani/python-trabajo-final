from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    consulta = request.GET.get('consulta')
    if consulta:
        productos = models.Producto.objects.filter(name__icontains=consulta)
    else:
        productos = models.Producto.objects.all()
    context = {
        'productos': productos,
        'consulta_actual': consulta
    }
    if 'limpiar' in request.GET:  
        return redirect('producto:home')
    return render(request, 'producto/index.html', context)

def categoria_create(request):
  if request.method == 'POST':
    form = forms.CategoriasForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('producto:home')
  else:
    form = forms.CategoriasForm()
    
  return render(request, 'producto/categoria_create.html', {'form': form})

def producto_create(request):
  if request.method == 'POST':
    form = forms.ProductoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('producto:home')
  else:
    form = forms.ProductoForm()
    
  return render(request, 'producto/producto_create.html', {'form': form})