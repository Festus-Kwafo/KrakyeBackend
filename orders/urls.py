from django.urls import path
from . import views

app_name   = 'orders'

urlpatterns = [
    path('', views.order_register, name='order_register'),
    path('invoice/', views.invoice, name='invoice'),
    path('add/', views.add, name='add'),
]


    
