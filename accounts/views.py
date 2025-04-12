"""
This module contains the view functions for the Soccer School application.

Functions:
    home(request):
        Handles requests to the home page and returns a simple welcome message.

    about(request):
        Handles requests to the about page and returns information about the Soccer School.
"""

# Django imports
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Local imports
from .forms import CustomAuthenticationForm


# Create your views here.
def login_view(request):
    """
    Handles the user login process.
    This view is responsible for rendering the login page
    or processing login-related requests.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: A rendered login page.
    """
    context = {}
    template_name = "accounts/login.html"
    if request.method == "POST":
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")  # Redirect to profile page on success

        messages.warning(request, "Invalid username or password...!!!")
        context = {"form": form}
        return render(request, "accounts/login.html", context)
    form = CustomAuthenticationForm()
    context = {"form": form}

    return render(request, template_name, context)


@login_required
def logout_view(request):
    """
    Handles the user logout process.
    This view is responsible for rendering the logout page
    or processing logout-related requests.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: A rendered logout page.
    """
    logout(request)
    return redirect("login")  # Redirect to login page after logout


def register_view(request):
    """
    Handles the user registration process.
    This view is responsible for rendering the registration page
    or processing registration-related requests.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: A rendered registration page.
    """
    template_name = "accounts/register.html"
    context = {}
    return render(request, template_name, context)


def profile_view(request, user_id):
    """
    Renders the profile page for a user.
    Args:
        request (HttpRequest): The HTTP request object.
        user_id (int): The ID of the user whose profile is being viewed.
    Returns:
        HttpResponse: The rendered profile page.
    Context:
        - If the user is authenticated:
            - user_profile (dict): A dictionary containing the user's profile information:
                - username (str): The username of the authenticated user.
                - email (str): The email address of the authenticated user.
                - first_name (str): The first name of the authenticated user.
                - last_name (str): The last name of the authenticated user.
        - If the user is not authenticated:
            - error (str): An error message indicating the user is not authenticated.
    """

    template_name = "accounts/profile.html"
    context = {}
    try:
        user = User.objects.get(pk=user_id)
        context["user_profile"] = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    except User.objects.model.DoesNotExist:
        context["error"] = "User does not exist."
    return render(request, template_name, context)
