from django.contrib import admin
from .models import Product, Category, Brand

# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
# This code registers the Product model with the Django admin site, allowing it to be managed through the admin interface.
# This is useful for managing products in an e-commerce application, where you can add, edit, or delete products directly from the admin dashboard.
# The Product model includes fields for name, description, price, stock, and timestamps for creation and updates.
# This allows administrators to easily manage the product catalog of the store.
