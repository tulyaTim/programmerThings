from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class createMessage(models.Model):
    message = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
