from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from catalogo.models import Product

class Order(models.Model):
  client = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
  quantity = models.PositiveIntegerField()
  total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
  order_date = models.DateTimeField(default=timezone.now, editable=False)

  class Meta:
    ordering = ['-order_date']

  def clean(self):
    if self.quantity > self.product.stock:
      raise ValidationError('La cantidad solicitada supera el stock disponible.')
    
  def save(self, *args, **kwargs):
    self.total_price = self.product.price * self.quantity
    super().save(*args, **kwargs)
