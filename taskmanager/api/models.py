from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=32, default='', unique=True)
    full_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    telegram_name = models.CharField(max_length=64, default='')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']
