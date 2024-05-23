from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'clientes'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('cliente/<int:pk>/update', views.ClientUpdate.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/detail', views.ClienteDetail.as_view(), name='cliente_detail'),
]

urlpatterns += staticfiles_urlpatterns()