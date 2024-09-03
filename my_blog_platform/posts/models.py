from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CreatePost(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    about_post = models.CharField(max_length=255, null=False)
    # img = models.ImageField(upload_to="uploads/images", blank=True, null=True)

    def __str__(self):
        return self.about_post
