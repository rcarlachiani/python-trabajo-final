from django.db import models

class User(models.Model):
  username = models.CharField(max_length=100, verbose_name='Nombre de usuario')
  password = models.CharField(max_length=100, verbose_name='Contraseña')

  def __str__(self):
    return self.username

class Client(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  surname = models.CharField(max_length=100, verbose_name='Apellido')
  date = models.DateField(verbose_name='Fecha de nacimiento')
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
  email = models.EmailField(verbose_name='Email')

  def __str__(self):
    return f"{self.surname}, {self.name}"
