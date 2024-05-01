from django.db import models

class Categorias(models.Model):
  name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')

  def __str__(self):
    return self.name
  
class Formatos(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name
  
class Producto(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  price = models.IntegerField(verbose_name='Precio')
  category = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name='Categoría')

  def __str__(self):
    return f"{self.name} - {self.category} - U$S{self.price}"