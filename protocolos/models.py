from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Product(models.Model):
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição")
    price = models.FloatField("Preço")
    size = models.IntegerField("Tamanho")
    color = models.CharField("Cor", max_length=50)
    stock_quantity = models.PositiveIntegerField("Quantidade em Estoque", default=0)
    category = models.ForeignKey(Category, verbose_name="Categoria", on_delete=models.PROTECT)
    image = models.URLField("URL da Imagem")

    def __str__(self):
        return self.name

    def get_stock_quantity(self):
        stock = getattr(self, 'stock', None)
        if stock:
            return stock.quantity
        return 0

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Review(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Produto", on_delete=models.CASCADE)
    rating = models.IntegerField("Avaliação")
    description = models.TextField("Descrição")

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rating})"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Stock(models.Model):
    product = models.OneToOneField(Product, verbose_name="Produto", on_delete=models.CASCADE, related_name='stock')
    quantity = models.IntegerField("Quantidade", default=0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"


class Cart(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE, related_name='cart')
    total_price = models.FloatField("Preço Total", default=0.0)

    def __str__(self):
        return f"{self.user.username}'s Cart"

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="Carrinho", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Produto", on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantidade")

    def __str__(self):
        return f"{self.cart.user.username} - {self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "Produto do Carrinho"
        verbose_name_plural = "Produtos do Carrinho"


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.PROTECT)
    date = models.DateTimeField("Data", auto_now_add=True)
    status = models.CharField("Status", max_length=50)
    delivery_address = models.CharField("Endereço de Entrega", max_length=255)
    total_price = models.FloatField("Preço Total")

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

    class Meta:
        ordering = ["-date"]
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name="Pedido", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Produto", on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantidade")

    def __str__(self):
        return f"{self.order.user.username} - {self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "Produto do Pedido"
        verbose_name_plural = "Produtos do Pedido"


class Payment(models.Model):
    order = models.OneToOneField(Order, verbose_name="Pedido", on_delete=models.CASCADE)
    payment_method = models.CharField("Método de Pagamento", max_length=50)
    payment_status = models.CharField("Status do Pagamento", max_length=50)
    value = models.FloatField("Valor")

    def __str__(self):
        return f"{self.order.user.username} Payment - ${self.value:.2f}"

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
