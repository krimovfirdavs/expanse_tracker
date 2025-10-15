from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

import src.template_views.forms as forms


class RegisterUserView(CreateView):
    model = User
    form_class = forms.RegisterUserForm
    template_name = "auth/forms.html"
    success_url = "/"


class LoginUserView(LoginView):
    template_name = "auth/forms.html"
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


class LogoutUserView(LogoutView):
    next_page = "/"
