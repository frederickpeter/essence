from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    date_verified = models.DateTimeField(null=True)

    USERNAME_FIELD = "email"
    # username field cannot be part of required fieldss
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        return self.email
    
    class Meta:
        ordering = ["first_name"]
