from django.conf import settings
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


class Organization(models.Model):
    name = models.CharField(max_length=64, default='', unique=True)
    admin_id = models.IntegerField()


class Organization_Users(models.Model):
    role = models.CharField(max_length=32, default='', unique=True)
    organization = models.ManyToManyField(Organization)


class Project(models.Model):
    name = models.CharField(max_length=64, default='')
    organization = models.ManyToManyField(Organization)


class Project_Users(models.Model):
    role = models.CharField(max_length=32, default='', unique=True)
    project = models.ManyToManyField(Project)
