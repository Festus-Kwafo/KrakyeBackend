from django.conf import settings
from django.db import models
from django.forms import FloatField
from django.utils.html import mark_safe
from django.urls import reverse
from category.models import Category

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_stock=True)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # size = models.CharField(max_length=30, choices=SIZES)
    # color = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    size_guide = models.ImageField(upload_to='size_guide/')
    images = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    stock = models.IntegerField(default=0) 
    in_stock = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    objects = models.Manager()
    products = ProductManager()

    @property
    def discount(self):
        if self.discounted_price > 0:
            discount_percent = ((self.price - self.discounted_price)/self.price)*100
            return format(discount_percent, '.2f')

    # def image_tag(self):
    #         return mark_safe('<img src="/media/%s" width="90" height="90" />' % (self.image))
    # image_tag.short_description = 'Image'

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.category.slug, self.slug])
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_date', )

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choices = (
    ('color', 'color'),
    ('size', 'size'),

)
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choices)
    variation_value = models.CharField(max_length=100,)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()
    
    def __str__(self):
        return self.variation_value
