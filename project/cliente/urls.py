from django.urls import path
from . import views

app_name = 'cliente'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('usuario/create/', views.usuario_create, name='usuario_create'),
    path('cliente/create/', views.cliente_create, name='cliente_create'),
]