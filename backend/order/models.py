import os
import pdfkit
import uuid

from django.core.files.base import File
from django.db import models
from django.template.loader import render_to_string
from django.utils.timezone import now


prices = {
    100: 3.69,
    200: 3.61,
    300: 3.53,
    400: 3.41,
    500: 3.35,
    600: 3.31,
    700: 3.25,
    800: 3.21,
    900: 3.18,
    1000: 3.15
}


def get_volume_price(amount):

    keys = sorted(list(prices.keys()), key=lambda x: x)
    for key in keys:
        if key >= amount:
            return prices.get(key)


class Order(models.Model):
    """
    Order details
    """
    quantity = models.IntegerField(verbose_name='Daudzums')
    verbose_id = models.CharField(unique=True, max_length=20)

    # person_type = models.

    name = models.CharField(max_length=200, verbose_name='Vārds, uzvārds/Nosaukums')
    legal_address = models.TextField(verbose_name='Juridiskā adrese')
    shipment_address = models.TextField(blank=True, null=True, verbose_name='Piegādes adrese (ja atšķiras no juridiskās)')

    bank = models.CharField(max_length=100, verbose_name='Banka')
    swift = models.CharField(max_length=50, verbose_name='Bankas SWIFT kods')
    account_iban = models.CharField(max_length=50, verbose_name='Konta numurs (IBAN)')

    phone = models.CharField(max_length=50, verbose_name='Tālrunis')
    email = models.EmailField('Epasts')

    payment_date = models.DateTimeField(blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)

    generate_invoice = models.BooleanField(default=False, editable=False)
    invoice = models.FileField(upload_to='invoices', blank=True, null=True)

    def generate_verbose_id(self):
        date_string = now().strftime('%d/%m/%Y')
        return '{0}-{1}'.format(
            date_string,
            self.__class__.objects.filter(verbose_id__startswith=date_string).count()
        )

    def make_invoice(self):

        file_name = '{0}.pdf'.format(uuid.uuid4())
        template = render_to_string('order/invoice.html', {'obj': self})
        pdf_options = {
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-bottom': '0',
            'margin-left': '0',
            'encoding': 'UTF-8',
        }
        pdfkit.from_string(template, file_name, options=pdf_options)

        self.generate_invoice = False
        self.invoice.save(file_name, File(open(file_name, 'rb')))
        os.remove(file_name)

    def save(self, *args, **kwargs):
        if not self.verbose_id:
            self.verbose_id = self.generate_verbose_id()

        super().save(*args, **kwargs)
        if self.generate_invoice:
            self.make_invoice()
