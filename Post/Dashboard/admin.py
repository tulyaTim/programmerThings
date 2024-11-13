from django.contrib import admin
from .models import Post, Message, Chat

# Register your models here.
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Chat)
