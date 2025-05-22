from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Stock, Product

@receiver(post_save, sender=Stock)
def update_product_stock_quantity(sender, instance, **kwargs):
    product = instance.product
    product.stock_quantity = instance.quantity
    product.save()