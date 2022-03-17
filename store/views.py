from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def all_products(request):
    categories = Category.objects.all()
    products    = Product.objects.all().order_by('id')[:8]
    new_arrivals = Product.objects.all().order_by('id')
    return render(request, 'index.html', {'products': products, 'categories': categories, 'new_arrivals': new_arrivals })



    