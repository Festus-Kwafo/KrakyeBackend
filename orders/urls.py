from django.urls import path
from . import views

app_name   = 'orders'

urlpatterns = [
    #path('', views.order_register, name='order_register'),
    path('invoice/', views.invoice, name='invoice'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('country-json/', views.get_json_country_data, name='country-json'),
    path('country-json/<str:country>/', views.get_json_city_data, name='city-json'),
    path('add/', views.add, name='add'),
    #path('update/', views.update, name='update'),
]


    
