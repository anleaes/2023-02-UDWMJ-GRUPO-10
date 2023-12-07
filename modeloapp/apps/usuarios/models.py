from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)