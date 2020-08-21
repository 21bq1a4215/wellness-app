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
        'stripe_public_key' : 'pk_test_51HC8P1Heew9pZh4QWYPg5l1n5w0nIhn5VDBJXZdFmdY0WOKKC1A6HOOCx7Atxl8EvVT8jjUGbPACB70i184RIXc700jmxSpNMl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)