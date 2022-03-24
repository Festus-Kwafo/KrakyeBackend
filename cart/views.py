from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def cart_summary(request):
    return render(request, 'store/cart/cart.html' )

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
    

