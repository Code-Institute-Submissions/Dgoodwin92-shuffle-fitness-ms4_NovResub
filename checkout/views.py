from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_publice_key': 'pk_test_51JiQm0E9SMmhosMA1BiFYiRi8BmGWB9iSaTKCgaZdu6ehQeeBy8vOPPMu1Fjw9X3V7Y3pLiqVElSMqErtKYTvnKd00XMMAEjVy',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)