from django import forms 
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name..'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(123) 456-7890'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message here...',
                'style': 'height: 10rem;'
            }),
        }
        labels = {
            'name': 'Full name',
            'email': 'Email address',
            'phone': 'Phone number',
            'message': 'Message',
        }