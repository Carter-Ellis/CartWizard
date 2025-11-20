from django.contrib import admin
from .models import Product, Category, Inventory, Cart, CartItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(Cart)
admin.site.register(CartItem)
