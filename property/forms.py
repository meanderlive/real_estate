from django import forms
from .models import ContactAgents
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ContactAgentForm(forms.ModelForm):
    class Meta:
        model = ContactAgents
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']