from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    subtitle = models.CharField(max_length=300)
    bio = models.TextField(max_length=500)
    image = models.ImageField(upload_to="uploads/author_bio")
