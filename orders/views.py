
from unicodedata import name
from urllib import request, response
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, Address
from cart.cart import Cart
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from .forms import CheckoutForm
from cities_light.models import Country, City
from payments.models import Payment
# Create your views here.

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class CheckoutView(View):
    def get(self, *args, **kwargs):
        
        try:
            order = Order.objects.get_or_create(user=self.request.user)
            countries_qs = Country.objects.all()
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order,
                'countries_qs': countries_qs
            }

            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='S',
                default=True
            )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='B',
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
            
            return render(self.request, "store/order/checkout.html", context)

        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("orders:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user)
            if form.is_valid():

                use_default_shipping = form.cleaned_data.get(
                    'use_default_shipping')
                if use_default_shipping:
                    print("Using the defualt shipping address")
                    address_qs = Address.objects.filter(
                        user=self.request.user,
                        address_type='S',
                        default=True
                    )
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default shipping address available")
                        return redirect('orders:checkout')
                else:
                    print("User is entering a new shipping address")
                    shipping_first_name = form.cleaned_data.get(
                        'billing_first_name')
                    shipping_last_name = form.cleaned_data.get(
                        'billing_first_name')
                    shipping_address1 = form.cleaned_data.get(
                        'shipping_address')
                    shipping_address2 = form.cleaned_data.get(
                        'shipping_address2')
                    shipping_country = form.cleaned_data.get(
                        'shipping_country')
                    shipping_zip = form.cleaned_data.get('shipping_zip')

                    if is_valid_form([shipping_address1, shipping_country, shipping_zip, shipping_last_name, shipping_first_name ]):
                        shipping_address = Address(
                            user=self.request.user,
                            first_name = shipping_first_name,
                            last_name = shipping_last_name,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            address_type='S'
                        )
                        shipping_address.save()

                        order.shipping_address = shipping_address
                        order.save()

                        set_default_shipping = form.cleaned_data.get(
                            'set_default_shipping')
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()

                    else:
                        messages.info(
                            self.request, "Please fill in the required shipping address fields")

                use_default_billing = form.cleaned_data.get(
                    'use_default_billing')
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address')

                if same_billing_address:
                    billing_address = shipping_address
                    billing_address.pk = None
                    billing_address.save()
                    billing_address.address_type = 'B'
                    billing_address.save()
                    order.billing_address = billing_address
                    order.save()

                elif use_default_billing:
                    print("Using the defualt billing address")
                    address_qs = Address.objects.filter(
                        user=self.request.user,
                        address_type='B',
                        default=True
                    )
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        order.billing_address = billing_address
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default billing address available")
                        return redirect('orders:checkout')
                else:
                    print("User is entering a new billing address")
                    billing_first_name = form.cleaned_data.get(
                        'billing_first_name')
                    billing_last_name = form.cleaned_data.get(
                        'billing_last_name')
                    billing_address1 = form.cleaned_data.get(
                        'billing_address')
                    billing_address2 = form.cleaned_data.get(
                        'billing_address2')
                    billing_country = form.cleaned_data.get(
                        'billing_country')
                    billing_zip = form.cleaned_data.get('billing_zip')

                    if is_valid_form([billing_address1, billing_country, billing_zip, billing_last_name, billing_first_name]):
                        billing_address = Address(
                            user=self.request.user,
                            first_name= billing_first_name, 
                            last_name=billing_last_name,
                            street_address=billing_address1,
                            apartment_address=billing_address2,
                            country=billing_country,
                            zip=billing_zip,
                            address_type='B'
                        )
                        billing_address.save()

                        order.billing_address = billing_address
                        order.save()

                        set_default_billing = form.cleaned_data.get(
                            'set_default_billing')
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()

                    else:
                        messages.info(
                            self.request, "Please fill in the required billing address fields")

                payment_option = form.cleaned_data.get('payment_option')

                if payment_option == 'M':
                    return redirect('payments:initiate-payment')
                elif payment_option == 'C':
                    return redirect('payments:initiate-payment')
                else:
                    messages.warning(
                        self.request, "Invalid payment option selected")
                    return redirect('orders:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("cart:cart_summary")

    def countries_view(self):
        countries_qs = Country.objects.all()
        return render(self.request, 'store/order/checkout.html', {'countries_qs': countries_qs})    


@login_required
def invoice(request):
    user_id = request.user.id
    order_confirm = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    cart = Cart(request)
    cart.clear()
    return render(request, 'store/order/confirmation.html',{ 'order_confirm':order_confirm})



def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders

def get_json_country_data(request):
    qs_val = list(Country.objects.values())
    return JsonResponse({'data':qs_val})

def get_json_city_data(request,  *args, **kwargs):
    selected_country =kwargs.get('country')
    obj_city = list(City.objects.filter(country__name=selected_country).values())
    return JsonResponse( {'data': obj_city})


def add(request):
    cart = Cart(request)    
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        carttotal = cart.get_total_price()
        status = request.POST.get('status')        
        if Order.objects.filter(user_id=user_id).exists():
            Order.objects.update(order_key=order_key, user_id=user_id)
        else:
            Order.objects.update_or_create(order_key=order_key, user_id=user_id)
            
        for item in cart:            
            OrderItem.objects.create(product=item['product'], price=item['price'], quantity=item['qty'])

        if Payment.objects.filter(order_key=order_key).exists():
            pass
        else:
            Payment.objects.create(order_key=order_key)
        if status == "success":
            Order.objects.filter(order_key=order_key).update(billing_status=True)
            Payment.objects.filter(order_key=order_key).update(verified=True)
            Payment.objects.filter(order_key=order_key).update(amount=carttotal)
            Payment.objects.filter(order_key=order_key).update(user_id=user_id)
        print(status)

        response = JsonResponse({'success':'Return Something'})
        return response 

