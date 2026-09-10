from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['service', 'name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        