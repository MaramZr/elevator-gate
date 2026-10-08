from django import forms
from .models import ContactMessage
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "service",
            "subject",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "أدخل اسمك الكامل",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "username@domain.com",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "05xxxxxxxx",
                }
            ),

            "service": forms.Select(),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "موضوع الاستفسار",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": "اكتب هنا تفاصيل طلبك لمساعدتنا في خدمتك بشكل أفضل...",
                    "rows": 6,
                }
            ),
        }