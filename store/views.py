from django.shortcuts import render, get_object_or_404

from cart.views import cart_summary
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from backend.settings import AUTH_USER_MODEL
from cities_light.models import Country
from cart.cart import Cart
from category.models import *
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products    = Product.objects.filter(in_stock=True).order_by('id')[:10]
    top_sale    = Product.objects.filter(in_stock=True).order_by('-price')[:10]
    new_arrivals = Product.objects.all().order_by('-created_date')[:5]
    countries_qs = Country.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories, 'new_arrivals': new_arrivals, 'top_sale': top_sale, 'countries_qs': countries_qs })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    related_product = Product.objects.filter(
        category=product.category).exclude(slug=slug)
    cart = Cart(request)
    product_in_cart = cart_summary
    return render(request, 'store/product/product.html', {'product': product, 'related': related_product, 'cart':product_in_cart})


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


def about_us(request):
    return render(request, 'store/about_us.html')