from django.contrib import admin
from .models import Images, Product, Category

#Register Model on Admin Panel

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug',
                    'new_price', 'old_price', 'in_stock', 'created', 'updated', 'category']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['new_price', 'old_price', 'in_stock']
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Images)
