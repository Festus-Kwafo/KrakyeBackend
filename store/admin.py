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

admin.site.register(Product, ProductAdmin)


