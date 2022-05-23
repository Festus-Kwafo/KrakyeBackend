from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from store.models import Product
from cities_light.models import Country


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class Order(models.Model):
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
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
class Address(models.Model):

    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    street_address = models.CharField(max_length=225, null=True)
    apartment_address = models.CharField(max_length=225, null=True)
    country = models.CharField(max_length=255, null=True)
    zip = models.CharField(max_length=225, null=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES, null=True)
    default = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'
 
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