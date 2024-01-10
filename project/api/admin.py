from django.contrib import admin
from .models import Products, Categories

class ProductsAdmin(admin.ModelAdmin):
    order = ['name']
    list_display = ['name', 'price', 'quantity', 'unit']

admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories)

