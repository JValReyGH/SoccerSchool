"""
This module defines the models for the accounts application.

Classes:
    Profile: Extends the default Django User model with additional fields
        such as name, age, gender, email, birth date, weight, height,
        current team, and avatar.

Dependencies:
    - django.db.models: Provides the base classes for defining database models.
    - django.contrib.auth.models.User: The built-in Django User model for authentication.

Usage:
    The Profile model is designed to store additional user information
    for a soccer school application. It includes fields for personal
    details, physical attributes, and optional fields for team and avatar.
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Represents a user profile in the soccer school application.
    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model.
        name (CharField): The full name of the user, limited to 100 characters.
        age (PositiveIntegerField): The age of the user.
        gender (CharField): The gender of the user, with choices of "Male", "Female", or "Other".
        email (EmailField): The unique email address of the user.
        birth_date (DateField): The birth date of the user.
        weight (FloatField): The weight of the user in kilograms.
        height (FloatField): The height of the user in meters.
        current_team (CharField): The name of the user's current team, optional.
        avatar (ImageField): An optional profile picture for the user, stored in the "avatars/" directory.
    Methods:
        __str__(): Returns the string representation of the profile, which is the user's name.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
    )
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    current_team = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the object.
        This method is used to provide a human-readable representation
        of the object, typically for debugging or display purposes.
        Returns:
            str: The name of the object.
        """

        return str(self.name)
