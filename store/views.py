from turtle import title
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, View
from django.core import serializers
from .models import Category, Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/index.html',  {'products': products})
class HomeView(TemplateView):
    template_name = 'store/index.html'

class ProductView(View):
    def get(self, request):
        qs = Product.objects.all()
        data = serializers.serialize('json', qs)
        return JsonResponse({'data':data}, safe=False)
