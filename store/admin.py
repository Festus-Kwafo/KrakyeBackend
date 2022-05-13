from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_header = 'Krakye Clothing Admin'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'stock', 'category', 'discount', 'in_stock', 'created_date',    ]
    list_filter = ['in_stock',]
    list_editable = ['stock', 'in_stock']
    prepopulated_fields = {'slug': ('product_name', )}
    field = ('price', 'stock', 'discount', 'image_tag')
    readonly_fields = ['discount', ]

class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'created_date', 'is_active']
    list_editable = ['is_active', ]
    list_filter = ['product', 'variation_category', 'variation_value',]
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)

