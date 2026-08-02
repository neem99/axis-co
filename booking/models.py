from django.db import models
from django.utils.timezone import now


# Create your models here.
# Lead table
class Lead(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"
