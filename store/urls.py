from unicodedata import name
from django.urls import path
from . import views

app_name   = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('shop/', views.shop, name='shop'), 
]


    
