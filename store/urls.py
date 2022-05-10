from unicodedata import name
from django.urls import path
from . import views

app_name   = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<str:category_slug>/', views.shop, name='products_by_category'),
    path('shop/<str:category_slug>/<str:product_slug>/', views.product_detail, name="product_detail"), 
    path('about-us/', views.about_us, name='about_us'), 
]


    
