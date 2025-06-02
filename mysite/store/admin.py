from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'available', 'stock', 'category', 'created_at', 'update_at', 'price', 'discoount', 'warranty')
    list_filter = ('available', 'category', 'price')
    prepopulated_fields = {'slug': ('name',)}