"""
Application model forms
"""
from django import forms
from localflavor.generic.forms import BICFormField, IBANFormField

from order import models


class OrderForm(forms.ModelForm):
    """
    Order form details
    """
    account_iban = IBANFormField(label='Konta numurs (IBAN)')
    swift = BICFormField(label='Bankas SWIFT kods')

    class Meta(object):
        model = models.Order
        fields = (
            'quantity',
            'name',
            'phone',
            'email',
            'legal_address',
            'shipment_address',
            'bank',
            'swift',
            'account_iban',
        )
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'col-5'}),
            'phone': forms.TextInput(attrs={'class': 'col-5'}),
            'email': forms.EmailInput(attrs={'class': 'col-5'}),
            'bank': forms.TextInput(attrs={'class': 'col-5'}),
            'swift': forms.TextInput(attrs={'class': 'col-5'}),
            'legal_address': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'shipment_address': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }
