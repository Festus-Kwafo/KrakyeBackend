from django.shortcuts import render

from store import views
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart_summary(request):
    cart = Cart(request)
    return render(request,  'store/cart/cart.html', {'cart':cart} )

@csrf_exempt
def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product, qty=product_qty)
        
        cartqty = cart.__len__()
        response = JsonResponse({'qty' : cartqty})
        return response
    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id) 
        
        carttotal  = cart.get_total_price()
        cartqty = cart.__len__()
        response = JsonResponse({'subtotal': carttotal,'qty' : cartqty})
        return response