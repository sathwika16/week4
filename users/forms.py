from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  # or just import User if not using CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser  # Use CustomUser if defined, otherwise just User
        fields = ('username', 'email')  # Add 'email' if using CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    pass