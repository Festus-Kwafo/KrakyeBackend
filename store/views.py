from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from cart.models import CartItem
from cart.views import _cart_id
from .models import *
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from backend.settings import AUTH_USER_MODEL
from category.models import *
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products    = Product.objects.filter(in_stock=True).order_by('id')[:10]
    top_sale    = Product.objects.filter(in_stock=True).order_by('-price')[:10]
    new_arrivals = Product.objects.all().order_by('-created_date')[:5]
    context = {
        'products': products, 
        'categories': categories, 
        'new_arrivals': new_arrivals, 
        'top_sale': top_sale,
        }
    return render(request, 'index.html', context)


def product_detail(request, category_slug=None, product_slug=None):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        new_arrivals = Product.objects.all().order_by('-created_date')[:5]
    except Exception as e:
        raise e
   
    context = {
        'single_product':single_product,
        'in_cart':in_cart,
        'new_arrivals': new_arrivals, 
        }
    return render(request, 'store/product/product.html', context )

def product_by_category(request, category_slug=None):
    product_category = Category.objects.all()
    category = Category.objects.get(slug = category_slug )    
    
    product = Product.objects.filter(category = category)
    product_count = product.count()
    paginator = Paginator(product, 20)
    page = request.GET.get('page')
    
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        product = paginator.page(paginator.num_pages)

    context = {
        'product_category': product_category,
        'product_count': product_count,
        'pages'  : page,
        'shop_products': product,
    }
    return render(request, 'store/shop.html', context)

def shop(request, category_slug=None):
    shop_products = None
    categories = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        shop_products = Product.objects.filter(category = categories, in_stock=True).order_by('?')
        product_count = Product.objects.count()
    else:
        shop_products  = Product.objects.all().order_by('?')
        product_count = Product.objects.count()

    paginator = Paginator(shop_products, 20)
    page = request.GET.get('page')
    
    try:
        shop_products = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        shop_products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        shop_products = paginator.page(paginator.num_pages)
    product_category = Category.objects.all()   
    context = {
        'shop_products': shop_products, 
        'pages'  : page ,
        'product_count': product_count,
        'product_category': product_category
    }
    return render(request, 'store/shop.html', context)


def about_us(request):
    return render(request, 'store/about_us.html')

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            shop_products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = shop_products.count()
    context = {
        'shop_products':shop_products,
        'product_count':product_count,
    }
    return render(request, 'store/shop.html', context)

def my_custom_page_not_found_view(request):
    return JsonResponse({"data": "Not found"})

def my_custom_page_not_found(request):
    return JsonResponse({"data": "Not found"})
