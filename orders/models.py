from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from store.models import Product
from django_countries.data import COUNTRIES
from address.models import AddressField

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user', null=True)
    full_name = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    address = AddressField(null=True)
    location = models.CharField(max_length=250, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    address_line_1 = models.CharField(max_length=150, blank=True, null=True)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    town_city = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    post_code = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    order_key = models.CharField(max_length=200, null=True, blank=True)
    billing_status = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
    complete =  models.BooleanField(default=False)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.created)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=1, null=True)

    def __str__(self):
        return str(self.id)