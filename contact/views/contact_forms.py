"""
This module contains the views for the contact application.
"""
from django.shortcuts import render
from contact.forms import ContactForm


def create(request):
    """Renders the create.html template for the contact application."""
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
