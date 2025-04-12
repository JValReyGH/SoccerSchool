"""
This module contains custom form classes for the accounts application. It extends
Django's built-in forms to provide additional functionality and customization for
user authentication.

Classes:
    CustomAuthenticationForm: A custom authentication form that adds a "remember_me"
    checkbox field and customizes the appearance of the form fields.

Usage:
    Import the `CustomAuthenticationForm` class and use it in your views or templates
    to render a login form with a "remember me" option and custom styling.

Example:

    def login_view(request):
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {'form': form})
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm
"""

from django import forms

from django.contrib.auth.forms import AuthenticationForm

from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    """
    A custom authentication form that extends Django's built-in AuthenticationForm.
    This form adds a "remember_me" checkbox field and customizes the appearance
    of the "username", "password", and "remember_me" fields by updating their
    widget attributes.
    Attributes:
        remember_me (forms.BooleanField): An optional checkbox field to allow
            users to indicate whether they want to be remembered on the device.
    Methods:
        __init__(*args, **kwargs): Initializes the form and updates the widget
            attributes for the fields to include custom CSS classes and placeholders.
    """

    remember_me = forms.BooleanField(required=False, label="Remember Me")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Username"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )
        self.fields["remember_me"].widget.attrs.update({"class": "form-check-input"})
