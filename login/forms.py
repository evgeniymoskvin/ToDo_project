from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, Select, PasswordInput
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control", 'id': 'floatingInput', 'placeholder': 'Login'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control", 'id': 'floatingPassword',
                   'placeholder': 'Password'}),
    )
