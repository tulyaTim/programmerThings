from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()

    class Meta:
        verbose_name_plural = 'Notes'
