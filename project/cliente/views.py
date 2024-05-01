from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    consulta = request.GET.get('consulta')
    if consulta:
        cliente = models.Client.objects.filter(name__icontains=consulta)
    else:
        cliente = models.Client.objects.all()
    context = {
        'clientes': cliente,
        'consulta_actual': consulta
    }
    if 'limpiar' in request.GET:  
        return redirect('cliente:home')
    return render(request, 'cliente/index.html', context)

def usuario_create(request):
  if request.method == 'POST':
    form = forms.UsuarioForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('cliente:home')
  else:
    form = forms.UsuarioForm()
    
  return render(request, 'cliente/usuario_create.html', {'form': form})

def cliente_create(request):
  if request.method == 'POST':
    form = forms.ClienteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('cliente:home')
  else:
    form = forms.ClienteForm()
    
  return render(request, 'cliente/cliente_create.html', {'form': form})
