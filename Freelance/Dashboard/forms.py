from django import forms
from .models import Post, UserProfile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'profile_pic', 'bio']
        widgets = {
            'slug':forms.HiddenInput()
        }
