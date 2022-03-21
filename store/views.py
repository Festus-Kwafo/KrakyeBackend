from django.shortcuts import render
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def all_products(request):
    categories = Category.objects.all()
    products    = Product.objects.filter(is_active=True).order_by('id')[:10]
    top_sale    = Product.objects.filter(is_active=True).order_by('-sale_price')[:10]
    new_arrivals = Product.objects.all().order_by('-created')[:5]
    return render(request, 'index.html', {'products': products, 'categories': categories, 'new_arrivals': new_arrivals, 'top_sale': top_sale })

    
def shop(request):
    products = Product.objects.all().order_by('-id')
    paginator = Paginator(products, 30)
    page = request.GET.get('page')
    product_count = Product.objects.count()
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    return render(request, 'store/shop.html', {'products': products, page: 'pages', 'product_count': product_count})


from django.shortcuts import render, redirect
from store.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

    