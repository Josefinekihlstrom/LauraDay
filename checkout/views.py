from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IDqhsKST7IrZHIDd6QY7r3NTecSip5CazQtdrnoRcWEJYB9P1xNT4gtNRJOjnP9WesvOqU9F3WeLtbXyBTV3AiR00Jdeb7HDQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
