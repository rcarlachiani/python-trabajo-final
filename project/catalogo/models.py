from django.db import models
  
class Format(models.Model):
  name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')

  def __str__(self):
    return self.name
  
class Genre(models.Model):
  name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')

  def __str__(self):
    return self.name
  
class Product(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  price = models.IntegerField(verbose_name='Precio')
  format = models.ForeignKey(Format, on_delete=models.CASCADE, verbose_name='Formato')
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Género')
  stock = models.IntegerField(default=0, verbose_name='Stock')
  image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='Imagen')

  def __str__(self):
    return f"{self.name} - {self.format} - {self.genre} - U$S{self.price}"