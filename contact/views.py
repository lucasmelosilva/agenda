"""
This module contains the views for the contact application.
"""

from django.shortcuts import render


def index(request):
    """Renders the index.html template for the contact application."""

    return render(
        request,
        'contact/index.html'
    )
