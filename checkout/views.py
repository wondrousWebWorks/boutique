from django.shortcuts import render, reverse, redirect
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
        'stripe_public_key': 'pk_test_51GqPsYKP14WGiq4LBCGkpzDps5JORfc9euGYZUeYnUBmby6Uzqcg0KMqQTuNDFw1dOOXHG3h4XH0QBoAeACTd46V00lnRRF4t9',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
