from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest

    question = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 50,
            'class':
            'form-control'}),
        help_text="Maximum length is 254 characters."
    )
