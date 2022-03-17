from django.conf import settings
from django.db import models
from django.forms import FloatField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name   


class Product(models.Model):
    
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=30, choices=SIZES)
    color = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    size_guide = models.ImageField(upload_to='image/')
    image_one = models.ImageField(upload_to='image/')
    image_two = models.ImageField(upload_to='image/')
    image_three = models.ImageField(upload_to='image/')
    slug = models.SlugField(unique=True)
    list_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def discount(self):
        if self.sale_price > 0:
            discount_percent = ((self.list_price - self.sale_price)/self.list_price)*100
            return format(discount_percent, '.2f')

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created', )