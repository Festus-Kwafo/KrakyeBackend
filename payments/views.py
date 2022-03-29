from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.conf import settings
from pypaystack import Transaction, Customer, Plan
from cart.cart import Cart

from .models import *
from orders.models import Order
from . import forms
from django.contrib import messages
import payments
# Create your views here.


# @login_required
# def BasketView(request):
#   return render(request, 'payment/make_payment.html')
@login_required
def invoice(request):
    return render(request, 'payment/confirmation.html')

@login_required
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            order_delivery = Order.objects.filter(user=request.user)
        if order_delivery.exists():
            delivery_item = order_delivery
            return render(request, 'payment/make_payment.html',
                          {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY, 'order_delivery': order_delivery, 'delivery_item':delivery_item})
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'payment/initiate_payment.html',
                  {'payment_form': payment_form})

@login_required
def verify_payment(request, id):
    transaction = Transaction(authorization_key=settings.PAYSTACK_SECRET_KEY)
    response = transaction.verify(id)
    all_transaction = transaction.getone('id')
    print(all_transaction)
    data = JsonResponse(response, safe=False)
    print(data.status_code)
    return data
