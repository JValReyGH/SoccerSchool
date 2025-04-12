"""
URL configuration for the accounts app.

This module defines the URL patterns for the accounts app, mapping specific
routes to their corresponding view functions. The `app_name` variable is set
to "accounts" to enable namespacing of these URLs when used in templates or
other parts of the project.

Routes:
- /login/    : Maps to `views.login_view` for user login functionality.
- /logout/   : Maps to `views.logout_view` for user logout functionality.
- /register/ : Maps to `views.register_view` for user registration functionality.
- /profile/  : Maps to `views.profile_view` for displaying or editing user profiles.
"""

from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
]
