from itertools import product
from urllib import request, response
from django.shortcuts import render,redirect
from .forms import OrderForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart
from django.http.response import JsonResponse
from payments.models import Payment
# Create your views here.


@login_required
def order_register(request):
    orderForm = OrderForm()
    if request.method == 'POST':
        orderForm = OrderForm(request.POST)
        if orderForm.is_valid():
            #user = orderForm.save(commit=False)
            #user.user = request.user
            #user.save()
            #orderForm.save()
            return redirect('payments:initiate-payment')
    return render(request, 'store/order/order_forms.html', {'orderForm':orderForm})

 


@login_required
def invoice(request):
    user_id = request.user.id
    order_confirm = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    cart = Cart(request)
    cart.clear()
    return render(request, 'store/order/confirmation.html',{ 'order_confirm':order_confirm})

def update(request):
    if request.POST.get('action') == 'formspost':
        user_id = request.user.id
        fullName = request.POST.get('Fullname')
        Location = request.POST.get('Location')
        PhoneNumber = request.POST.get('PhoneNumber')
        Postcode = request.POST.get('Postcode')
        Address = request.POST.get('Address')
        print(fullName)
        if Order.objects.filter(full_name=fullName).exists():
            pass
        else:
            Order.objects.filter(full_name=fullName).create(user_id=user_id, full_name=fullName, postcode=Postcode,  location=Location, phone_number=PhoneNumber, address_line_1=Address)
    response = JsonResponse({'success':'Return Something'})
    return response

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
            order =Order.objects.get()
            OrderItem.objects.create(product=item['product'], price=item['price'], quantity=item['qty'])

        if Payment.objects.filter(order_key=order_key).exists():
            pass
        else:
            Payment.objects.create(order_key=order_key)
        if status == "success":
            Order.objects.filter(order_key=order_key).update(billing_status=True)
            Payment.objects.filter(order_key=order_key).update(verified=True)
            Payment.objects.filter(order_key=order_key).update(amount=carttotal)
        print(status)

        response = JsonResponse({'success':'Return Something'})
        return response 

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders