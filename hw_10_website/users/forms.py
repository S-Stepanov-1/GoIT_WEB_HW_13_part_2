from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=16, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

    email = forms.EmailField(max_length=100,
                             required=True,
                             widget=forms.TextInput())

    password1 = forms.CharField(max_length=16, required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    password2 = forms.CharField(max_length=16, required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
