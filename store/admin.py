from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_header = 'Krakye Clothing Admin'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'category', 
                    'sale_price', 'discount', 'in_stock', 'created',    ]
    list_filter = ['in_stock', 'is_active']
    list_editable = ['sale_price', 'in_stock']
    prepopulated_fields = {'slug': ('name', )}
    field = ('list_price', 'sale_price', 'discount', 'image_tag')
    readonly_fields = ['discount', 'image_tag',]

admin.site.register(Product, ProductAdmin)