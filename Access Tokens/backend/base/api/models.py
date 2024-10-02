from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    cover_pic = models.ImageField(upload_to='cover_pics/', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True) 
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency_level = models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], default=1)

    def __str__(self):
        return f"{self.name} - {self.get_proficiency_level_display()}"

