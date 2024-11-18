from django import forms
from .models import Message, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Type a message'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['username']