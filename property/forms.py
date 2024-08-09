from django import forms
from .models import ContactAgents

class ContactAgentForm(forms.ModelForm):
    class Meta:
        model = ContactAgents
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }