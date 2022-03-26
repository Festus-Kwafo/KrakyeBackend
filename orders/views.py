from django.shortcuts import render,redirect
from .forms import OrderForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Order
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
            return redirect('orders:delivery_details')
    return render(request, 'store/order/order_forms.html', {'orderForm':orderForm})

@login_required
def delivery_details(request):
    order_delivery = Order.objects.filter(user=request.user)
    return render(request, 'store/order/order_delivery.html', {'order_delivery':order_delivery})
    