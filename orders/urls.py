from django.urls import path
from . import views

app_name   = 'orders'

urlpatterns = [
    path('', views.order_register, name='order_register'),
    path('checkout/', views.delivery_details, name='delivery_details'),
]


    
