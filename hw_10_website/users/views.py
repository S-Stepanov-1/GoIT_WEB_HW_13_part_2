from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import LoginForm, SignUpForm


# Create your views here.
class LoginUserView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
    next_page = "/"


class SignUpUserView(CreateView):
    template_name = "users/signup.html"
    form_class = SignUpForm

    def get_success_url(self):
        return reverse("users:login")


class LogoutUserView(LogoutView):
    next_page = "/"


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'
