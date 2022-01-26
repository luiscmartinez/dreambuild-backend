from django.db import models

# Create your models here.


class Appointment(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    body = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email
