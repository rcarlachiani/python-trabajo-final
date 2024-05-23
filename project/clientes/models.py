from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    phone = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='project/core/static/core/img/avatar_default.webp', null=True, blank=True)
