"""
views.py

This module contains the view functions for the Soccer School application.

Functions:
    index(request): Renders the base template for the application.

Dependencies:
    - django.shortcuts.render: Used to render templates with context data.
"""

from django.shortcuts import render


def index(request):
    """
    Renders the base template for the index page.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered base.html template.
    """
    return render(request, "base.html", {})
