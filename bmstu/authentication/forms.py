from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BootstrapUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    # Add Bootstrap classes to form fields if needed
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
    }
