from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
