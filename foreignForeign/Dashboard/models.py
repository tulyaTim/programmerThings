from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=20)
    birthday = models.DateField()
    STATUS_CHOICES = [
        ('kampala', 'Kampala'),
        ('hoima', 'Hoima'),
        ('fort', 'Fort'),
    ]
    location = models.CharField(choices=STATUS_CHOICES, default='kampala', max_length=15)
    slug = models.SlugField(max_length=10)

class Skill(models.Model):
    prog_language = models.CharField(max_length=25)
    slug = models.SlugField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Gig(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=30)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    CATEGORY_CHOICES = [
        ('it', 'IT'),
        ('design', 'Design')
    ]
    field = models.CharField(choices=CATEGORY_CHOICES, default='it', max_length=15)
    slug = models.SlugField(max_length=10)



