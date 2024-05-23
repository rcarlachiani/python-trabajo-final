from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from catalogo import models
from . import models

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('core:home')

@login_required
def home(request):
  if request.user.is_staff:
    orders = models.Order.objects.all()
    return render(request, 'ordenes/index.html', {'ordenes': orders})
  else:
    cliente = request.user.client
    orders = models.Order.objects.filter(client=cliente)
    return render(request, 'ordenes/index.html', {'ordenes': orders})
  
@login_required
def create_order(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    quantity = request.POST.get('quantity', 1) 
    order = models.Order(
        client=request.user.client,
        product=product,
        quantity=int(quantity)
    )
    try:
        order.full_clean()
        order.save()
        return render(request, 'ordenes/order_success.html', {'producto': product, 'quantity': quantity})
    except ValidationError:
        return render(request, 'catalogo/product_detail.html', {'producto': product, 'error_message': 'La cantidad solicitada supera el stock disponible.'})
    
class OrderDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Order
  success_url = reverse_lazy('ordenes:home')