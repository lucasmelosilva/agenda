"""
This module contains the views for the contact application.
"""

from django.shortcuts import render
from contact.models import Contact


def index(request):
    """Renders the index.html template for the contact application."""
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }

    return render(
        request,
        'contact/index.html',
        context,
    )
