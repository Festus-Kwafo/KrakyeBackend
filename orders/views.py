from itertools import product
from urllib import response
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
            user = orderForm.save(commit=False)
            user.user = request.user
            user.save()
            orderForm.save()
            return redirect('payments:initiate-payment')
    return render(request, 'store/order/order_forms.html', {'orderForm':orderForm})


@login_required
def invoice(request):
    order_confirm = Order.objects.filter(id=8)
    return render(request, 'store/order/confirmation.html',{ 'order_confirm':order_confirm})


def add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        carttotal = cart.get_total_price()
        status = request.POST.get('status')
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(order_key=order_key)
        order_id =order.pk
        for item in cart:
            OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        if Payment.objects.filter(order_key=order_key).exists():
            pass
        else:
            Payment.objects.create(order_key=order_key)
        if status == "success":
            Order.objects.filter(order_key=order_key).update(billing_status=True)
            Payment.objects.filter(order_key=order_key).update(verified=True)
        print(status)
        response = JsonResponse({'success':'Return Something'})
        return response 

