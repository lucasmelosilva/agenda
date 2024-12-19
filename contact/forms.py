"""this module contains forms for contact application
"""

from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """This class represents a Django form for the Contact model.
    It includes fields for first_name, last_name, and phone, and overrides
    the clean() method to add two validation errors to the form."""

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        """
        Defines the Meta class for the ContactForm,
        which specifies the Django model and fields to be included in the form.
        """
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        """Overrides the `clean_first_name` method to validate the `first_name`
        field. If the `first_name` is equal to 'ABC', it adds a validation
        error to the `first_name` field with the message 'Veio do add_error'
        and the error code 'invalid'. Finally,
        it returns the cleaned `first_name` value."""

        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        return first_name
