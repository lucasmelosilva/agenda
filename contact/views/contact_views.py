"""
This module contains the views for the contact application.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact


def index(request):
    """Renders the index.html template for the contact application."""
    contacts = Contact.objects.all().order_by(
        '-id').filter(show=True)

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos |'
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
        'contact': result,
        'site_title': f'{result.first_name} {result.last_name} |'
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )


def search(request):
    """Renders the index.html template for the contact application."""
    search_value: str = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.all()\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
    )\
        .order_by('-id')\

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': f"Search - {search_value} |"
    }

    return render(
        request,
        'contact/index.html',
        context,
    )
