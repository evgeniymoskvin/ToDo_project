from django.contrib.auth.views import LoginView
from . import forms


class UserLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'login/login.html'



