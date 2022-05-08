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
            return render(request, 'payment/make_payment.html',
                          {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,})
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'payment/initiate_payment.html',
                  {'payment_form': payment_form})

def single_details(request):
    user_id = request.POST.user.id
    order_details = Order.objects.filter(user_id=user_id)
    return render(request, 'payment/make_payment.html', {'order_details': order_details} )


@login_required
def verify_payment(request, id):
    transaction = Transaction(authorization_key=settings.PAYSTACK_SECRET_KEY)
    response = transaction.verify(id)
    all_transaction = transaction.getone('id')
    print(all_transaction)
    data = JsonResponse(response, safe=False)
    print(data.status_code)
    return data


