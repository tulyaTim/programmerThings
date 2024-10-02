from django.db import models

# Create your models here.

class Members(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    member_phone = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now_add=True)
    member_profile_pic = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    member_slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Members'