from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class AuthorSignup(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = CustomUser
        fields = (
            "image",
            "username",
            "email",
            "subtitle",
            "bio",
            "password1",
            "password2",
        )
