from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    #path('add/', views.basket_add, name='basket_add'),
    #path('delete/', views.basket_delete, name='basket_delete'),

]