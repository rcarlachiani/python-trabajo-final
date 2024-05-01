from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:home'), name='logout'),
]