from django.contrib import admin
from webapp.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_title', 'category', 'price']
    list_filter = ['product_title', 'price']
    search_fields = ['product_title', 'category', 'price']
    exclude = []


admin.site.register(Product, ProductAdmin)
