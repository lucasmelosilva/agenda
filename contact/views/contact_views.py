"""
This module contains the views for the contact application.
"""

from django.shortcuts import render, get_object_or_404
from contact.models import Contact


def index(request):
    """Renders the index.html template for the contact application."""
    contacts = Contact.objects.all().order_by(
        '-id').filter(show=True)
    context = {
        'contacts': contacts
    }

    return render(
        request,
        'contact/index.html',
        context,
    )


def contact(request, contact_id):
    """Renders the contact.html template for the contact application."""
    # result = Contact.objects.get(pk=contact_id)
    result = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': result
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )
