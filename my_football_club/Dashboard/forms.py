from django import forms
from .models import Members

class Members_form(forms.ModelForm):
    class Meta:
        model = Members
        fields = ('first_name', 'last_name', 'member_phone', 'member_profile_pic')