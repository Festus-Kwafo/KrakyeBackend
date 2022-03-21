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
