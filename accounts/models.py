from django.db import models

from django.contrib.auth.models import AbstractUser

# # Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=30,unique=True)
    username=models.CharField(max_length=50,unique=True)
    REQUIRED_FIELDS=['email','phone']

    def __str__(self) -> str:
        return self.username



