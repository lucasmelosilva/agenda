"""this module contains forms for contact application
"""

from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """This class represents a Django form for the Contact model.
    It includes fields for first_name, last_name, and phone, and overrides
    the clean() method to add two validation errors to the form."""

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'clase-a classe-b',
                'placeholder': 'Digite qualquer coisa'
            }
        ),
        label='Primeiro Nome',
        help_text='Digite o primeiro nome do seu novo contato'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'clase-a classe-b',
        #     'placeholder': 'Digite qualquer coisa'
        # })

    class Meta:
        """
        Defines the Meta class for the ContactForm,
        which specifies the Django model and fields to be included in the form.
        """
        model = Contact
        fields = ('first_name', 'last_name', 'phone')
        # widgets = {
        #     'first_name': forms.Textarea(
        #         attrs={
        #             'class': 'clase-a classe-b',
        #             'placeholder': 'Digite qualquer coisa'
        #         }
        #     )
        # }

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
