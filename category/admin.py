from django.contrib import admin
from category.models import Category


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
admin.site.register(Category, CategoryModelAdmin)