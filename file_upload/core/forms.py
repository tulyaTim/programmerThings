from django import forms
from .models import Option

class Options(forms.Form):
    field = forms.ModelChoiceField(queryset=Option.objects.all(), empty_label=None)

