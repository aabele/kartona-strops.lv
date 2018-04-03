from django.views.generic import CreateView

from order import models
from order import forms


class CreateOrderView(CreateView):

    model = models.Order
    form_class = forms.OrderForm

    def form_valid(self, form):
        form.instance.generate_invoice = True
        return super().form_valid(form)
