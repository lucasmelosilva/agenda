"""
This module defines the Contact model,
which represents a contact in the application.
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    """The `Category` model represents a category in the application.
    It has a `name` field, which is a `CharField` with a maximum length
    of 50 characters."""
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    """The `Contact` model represents a contact in the application.
    It has the following fields:

    - `first_name`: The first name of the contact, as a `CharField`
    with a maximum length of 50 characters.
    - `last_name`: The last name of the contact, as a `CharField`
     with a maximum length of 50 characters. This field is optional
    (can be blank).
    - `phone`: The phone number of the contact, as a `CharField`
    with a maximum length of 50 characters.
    - `email`: The email address of the contact, as an `EmailField`
    with a maximum length of 250 characters. This field is optional
    (can be blank).
    - `create_date`: The date and time when the contact was created,
    as a `DateTimeField` with the default value of the current time.
    - `description`: A description of the contact, as a `TextField`.
    This field is optional (can be blank).
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
