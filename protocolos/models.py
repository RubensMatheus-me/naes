from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    size = models.IntegerField()
    color = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.URLField()

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rating})"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.cart.user.username} - {self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "Cart Product"
        verbose_name_plural = "Cart Products"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    delivery_address = models.CharField(max_length=255)
    total_price = models.FloatField()

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

    class Meta:
        ordering = ["-date"]


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order.user.username} - {self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "Order Product"
        verbose_name_plural = "Order Products"


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    value = models.FloatField()

    def __str__(self):
        return f"{self.order.user.username} Payment - ${self.value:.2f}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
