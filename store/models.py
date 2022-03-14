from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.db.models.fields import FloatField

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural= 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Images(models.Model):
    image_one = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/')
    image_three = models.ImageField(upload_to='images/')

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=255)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    old_price = models.DecimalField(max_digits=6, decimal_places=2)
    new_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percent = FloatField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def discount(self):
        if self.discount_percent > 0:
            discounted_price = self.old_price - self.new_price * self.discount_percent / 100
            return discounted_price
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    
