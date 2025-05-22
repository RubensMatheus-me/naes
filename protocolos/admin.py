from django.contrib import admin
from .models import Category, Product, Review, Stock, Cart, CartProduct, Order, OrderProduct, Payment

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Stock)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Payment)