from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractBaseUser vs AbstractUser
# AbstractBaseUser requires a very fine level of control & customization (meaning re-writing in order to get django magic aligned)
# AbstractUser subclasses AbstractBaseUser (better if we just want to add fields)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
