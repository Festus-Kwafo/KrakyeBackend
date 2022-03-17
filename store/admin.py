from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_one', 'category', 
                    'list_price', 'sale_price', 'in_stock', 'created', 'updated', ]
    list_filter = ['in_stock', 'is_active']
    list_editable = ['list_price', 'sale_price', 'in_stock']
    prepopulated_fields = {'slug': ('name', )}

    def dicount_show(self, instance):
        return instance.discount_price()

admin.site.register(Product, ProductAdmin)