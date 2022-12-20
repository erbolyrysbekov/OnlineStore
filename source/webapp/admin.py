from django.contrib import admin
from webapp.models import Product, Order


class OrderProductInlines(admin.TabularInline):
    model = Order.products.through


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'created_at']
    readonly_fields = ['created_at']
    inlines = (OrderProductInlines,)


admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
