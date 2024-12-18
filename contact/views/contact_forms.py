"""
This module contains the views for the contact application.
"""
from django.shortcuts import render, redirect
from contact.forms import ContactForm


def create(request):
    """Renders the create.html template for the contact application."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

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
