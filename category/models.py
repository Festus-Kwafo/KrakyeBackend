from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to = 'media/categories')

    def __str__(self):
        return self.category_name