from django.urls import path
from . import views

app_name = 'ordenes'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('order_create/product/<int:pk>/', views.create_order, name='order_create'),
    path('order_delete/<int:pk>/', views.OrderDelete.as_view(), name='order_delete'),
]