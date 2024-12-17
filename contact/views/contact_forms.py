"""
This module contains the views for the contact application.
"""
from django.shortcuts import render


def create(request):
    """Renders the create.html template for the contact application."""
    context = {}

    return render(
        request,
        'contact/create.html',
        context,
    )
