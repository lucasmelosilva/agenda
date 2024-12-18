"""this module contains forms for contact application
"""

from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """This class represents a Django form for the Contact model.
    It includes fields for first_name, last_name, and phone, and overrides
    the clean() method to add two validation errors to the form."""

    class Meta:
        """
        Defines the Meta class for the ContactForm,
        which specifies the Django model and fields to be included in the form.
        """
        model = Contact
        fields = ('first_name', 'last_name', 'phone')

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        return super().clean()
