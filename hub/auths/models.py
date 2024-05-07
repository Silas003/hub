from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    id=models.CharField(primary_key=True, max_length=15)
    email=models.EmailField(unique=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']