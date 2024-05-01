from django.contrib import admin
from store.models import Product


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'modified_date', 'is_available', 'stock', "category"]
admin.site.register(Product, ProductModelAdmin)