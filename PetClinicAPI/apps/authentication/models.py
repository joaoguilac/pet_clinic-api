from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

from PetClinicAPI.resources.base_model import BaseModel


class User(AbstractBaseUser, BaseModel):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'role']
    USERNAME_FIELD = 'email'

    class RoleChoices(models.TextChoices):
        VET = 'vet'
        ADMIN = 'admin'
        USER = 'user'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=RoleChoices.choices, default=RoleChoices.USER)

    objects = UserManager()

    class Meta():
        app_label = 'authentication'