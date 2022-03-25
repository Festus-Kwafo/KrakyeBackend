from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.conf import settings


from .models import *
from . import forms
from django.contrib import messages
import payments
# Create your views here.


# @login_required
# def BasketView(request):
#   return render(request, 'payment/make_payment.html')


def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'payment/make_payment.html',
                          {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'payment/initiate_payment.html',
                  {'payment_form': payment_form})


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Verification Succesful")
    else:
        messages.error(request, "Verifaction failed")
    return redirect('payment:initiate-payment')
