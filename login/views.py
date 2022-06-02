from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import forms


class UserLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'login/login.html'


class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy("login")
    template_name = 'login/signup.html'

