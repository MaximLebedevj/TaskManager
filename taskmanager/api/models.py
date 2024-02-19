import datetime

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
    description = models.TextField(default='', blank=True)
    creation_date = models.DateTimeField(
        default=datetime.datetime.now, blank=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    # organizations = models.Manager()


class UsersOrganizations(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=32, default='', unique=True)
    participation_date = models.DateTimeField(
        default=datetime.datetime.now, blank=True)


class Project(models.Model):
    name = models.CharField(max_length=64, default='')
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)


class UsersProjects(models.Model):
    role = models.CharField(max_length=32, default='', unique=True)
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
