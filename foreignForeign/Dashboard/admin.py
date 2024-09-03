from django.contrib import admin
from .models import Profile, Gig, Skill

# Register your models here.
admin.site.register(Profile)
admin.site.register(Gig)
admin.site.register(Skill)