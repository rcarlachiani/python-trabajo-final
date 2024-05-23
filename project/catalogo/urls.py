from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'catalogo'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('producto/create/', views.ProductCreate.as_view(), name='producto_create'),
    path('producto/<int:pk>/', views.ProductDetail.as_view(), name='producto_detail'),
    path('producto/<int:pk>/update/', views.ProductUpdate.as_view(), name='producto_update'),
    path('producto/<int:pk>/delete/', views.ProductDelete.as_view(), name='producto_delete'),
]

urlpatterns += [
    path('formato/create/', views.FormatCreate.as_view(), name='formato_create'),
    path('genero/create/', views.GenreCreate.as_view(), name='genero_create'),
]

urlpatterns += staticfiles_urlpatterns()