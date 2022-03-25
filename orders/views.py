from django.shortcuts import render
from .forms import OrderForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def order_register(request):
    if request.method == 'POST':
        orderForm = OrderForm(request.POST)
        
        if orderForm.is_valid():
           orderForm.save()
    else:
        orderForm = OrderForm(instance=request.user)

    return render(request, 'store/order/order_forms.html', {'orderForm':orderForm})
