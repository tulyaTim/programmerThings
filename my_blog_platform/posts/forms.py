from .models import CreatePost
from django import forms


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePost
        fields = ['about_post']
