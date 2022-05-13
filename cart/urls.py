from django.urls import path
from . import views

app_name   = 'cart'

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add_cart/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart_delete/<int:product_id>/<int:cart_item_id>', views.cart_delete, name='cart_delete'),
    path('cart_item_delete/<int:product_id>/<int:cart_item_id>', views.cart_item_delete, name='cart_item_delete'),
    path('delete/', views.cart_delete, name='cart_delete'),
]


    
