from .models import AddContact
from django import forms

class AddContactForm(forms.ModelForm):
    class Meta:
        model = AddContact
        fields = ['Name', 'phone_number', 'slug']
        widgets = {
            'slug':forms.HiddenInput()
        }
