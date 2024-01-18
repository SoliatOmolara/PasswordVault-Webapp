from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PasswordVault


class PasswordVaultForm(forms.ModelForm):
    website_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = PasswordVault
        fields = [
            'website_name',
            'website_link',
            'website_password',
            'date',
        ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
