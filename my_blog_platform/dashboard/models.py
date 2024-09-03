from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

# Create your models here.

class AddContact(models.Model):
    Name = models.CharField(default="",max_length=25, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    slug = models.SlugField(max_length=20, default="", null=True, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
