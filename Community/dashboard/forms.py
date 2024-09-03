from django import forms
from .models import UserProfile, Post

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'bio', 'profile_pic']

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
