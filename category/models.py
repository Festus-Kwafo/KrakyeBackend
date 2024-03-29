from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to = 'categories')

    def get_absolute_url(self):
        return reverse('store:products_by_category', args=[str(self.slug)])
    
    class Meta:
        verbose_name_plural ='categories'


    def __str__(self):
        return self.category_name