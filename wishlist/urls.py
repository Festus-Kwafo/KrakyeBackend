from django.urls import path
from . import views

app_name   = 'wishlist'

urlpatterns = [
    path('', views.wishlist_summary, name='wishlist_summary'),
    #path('add/', views.wishlist_add, name='wishlist_add'),
]
