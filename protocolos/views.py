from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import (Category, Product, Review, Stock, Cart, CartProduct, Order, OrderProduct, Payment)



class PaginaInicial(TemplateView):
    template_name = 'manager.html'

# -----------------------------
# Create Views
# -----------------------------

class CategoryCreate(CreateView):
    template_name = "manage/form-add.html"
    model = Category
    fields = ["name", "description"]
    success_url = reverse_lazy("listar-categoria")
    extra_context = {"title": "Cadastrar Categoria"}


class ProductCreate(CreateView):
    template_name = "manage/form-add.html"
    model = Product
    fields = ["name", "description", "price", "size", "color", "stock_quantity", "category", "image"]
    success_url = reverse_lazy("listar-produto")
    extra_context = {"title": "Cadastrar Produto"}


class ReviewCreate(CreateView):
    template_name = "manage/form-add.html"
    model = Review
    fields = ["user", "product", "rating", "description"]
    success_url = reverse_lazy("listar-avaliacao")
    extra_context = {"title": "Cadastrar Avaliação"}


class StockCreate(CreateView):
    template_name = "manage/form-add.html"
    model = Stock
    fields = ["product", "quantity"]
    success_url = reverse_lazy("listar-estoque")
    extra_context = {"title": "Cadastrar Estoque"}


class CartCreate(CreateView):
    template_name = "manage/form-add.html"
    model = Cart
    fields = ["user", "total_price"]
    success_url = reverse_lazy("listar-carrinho")
    extra_context = {"title": "Cadastrar Carrinho"}


class CartProductCreate(CreateView):
    template_name = "manage/form-add.html"
    model = CartProduct
    fields = ["cart", "product", "quantity"]
    success_url = reverse_lazy("listar-produto-carrinho")   
    extra_context = {"title": "Cadastrar Produto no Carrinho"}


class OrderCreate(CreateView):
    template_name = "manage/form-add.html"
    model = Order
    fields = ["user", "status", "delivery_address", "total_price"]
    success_url = reverse_lazy("listar-pedido")
    extra_context = {"title": "Cadastrar Pedido"}


class OrderProductCreate(CreateView):
    template_name = "manage/form-add.html"
    model = OrderProduct
    fields = ["order", "product", "quantity"]
    success_url = reverse_lazy("listar-produto-pedido")
    extra_context = {"title": "Cadastrar Produto no Pedido"}


class PaymentCreate(CreateView):
    template_name = "manage/form-add.html"
    model = Payment
    fields = ["order", "payment_method", "payment_status", "value"]
    success_url = reverse_lazy("listar-pagamento")
    extra_context = {"title": "Cadastrar Pagamento"}


# -----------------------------
# Update Views
# -----------------------------

class CategoryUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = Category
    fields = ["name", "description"]
    success_url = reverse_lazy("listar-categoria")
    extra_context = {"title": "Editar Categoria"}


class ProductUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = Product
    fields = ["name", "description", "price", "size", "color", "stock_quantity", "category", "image"]
    success_url = reverse_lazy("listar-produto")
    extra_context = {"title": "Editar Produto"}


class ReviewUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = Review
    fields = ["user", "product", "rating", "description"]
    success_url = reverse_lazy("listar-avaliacao")
    extra_context = {"title": "Editar Avaliação"}


class StockUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = Stock
    fields = ["product", "quantity"]
    success_url = reverse_lazy("listar-estoque")
    extra_context = {"title": "Editar Estoque"}


class CartUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = Cart
    fields = ["user", "total_price"]
    success_url = reverse_lazy("listar-carrinho")   
    extra_context = {"title": "Editar Carrinho"}


class CartProductUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = CartProduct
    fields = ["cart", "product", "quantity"]
    success_url = reverse_lazy("listar-produto-carrinho")
    extra_context = {"title": "Editar Produto do Carrinho"}


class OrderUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = Order
    fields = ["user", "status", "delivery_address", "total_price"]
    success_url = reverse_lazy("listar-pedido")
    extra_context = {"title": "Editar Pedido"}


class OrderProductUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = OrderProduct
    fields = ["order", "product", "quantity"]
    success_url = reverse_lazy("listar-produto-pedido")
    extra_context = {"title": "Editar Produto do Pedido"}


class PaymentUpdate(UpdateView):
    template_name = "manage/form-add.html"
    model = Payment
    fields = ["order", "payment_method", "payment_status", "value"]
    success_url = reverse_lazy("listar-pagamento")
    extra_context = {"title": "Editar Pagamento"}


# -----------------------------
# Delete Views
# -----------------------------

class CategoryDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = Category
    success_url = reverse_lazy("listar-categoria")
    extra_context = {"title": "Excluir Categoria"}


class ProductDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = Product
    success_url = reverse_lazy("listar-produto")
    extra_context = {"title": "Excluir Produto"}


class ReviewDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = Review
    success_url = reverse_lazy("listar-avaliacao")
    extra_context = {"title": "Excluir Avaliação"}


class StockDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = Stock
    success_url = reverse_lazy("listar-estoque")
    extra_context = {"title": "Excluir Estoque"}


class CartDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = Cart
    success_url = reverse_lazy("listar-carrinho")  
    extra_context = {"title": "Excluir Carrinho"}


class CartProductDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = CartProduct
    success_url = reverse_lazy("listar-produto-carrinho")
    extra_context = {"title": "Excluir Produto do Carrinho"}


class OrderDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = Order
    success_url = reverse_lazy("listar-pedido")
    extra_context = {"title": "Excluir Pedido"}


class OrderProductDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = OrderProduct
    success_url = reverse_lazy("listar-produto-pedido")
    extra_context = {"title": "Excluir Produto do Pedido"}


class PaymentDelete(DeleteView):
    template_name = "manage/form-delete.html"
    model = Payment
    success_url = reverse_lazy("listar-pagamento")
    extra_context = {"title": "Excluir Pagamento"}


# -----------------------------
# List Views
# -----------------------------

class CategoryList(ListView):
    template_name = "manage/lists/category.html"
    model = Category


class ProductList(ListView):
    template_name = "manage/lists/product.html"
    model = Product


class ReviewList(ListView):
    template_name = "manage/lists/review.html"
    model = Review


class StockList(ListView):
    template_name = "manage/lists/stock.html"
    model = Stock


class CartList(ListView):
    template_name = "manage/lists/cart.html"
    model = Cart


class CartProductList(ListView):
    template_name = "manage/lists/cart_product.html"
    model = CartProduct


class OrderList(ListView):
    template_name = "manage/lists/order.html"
    model = Order


class OrderProductList(ListView):
    template_name = "manage/lists/order_product.html"
    model = OrderProduct


class PaymentList(ListView):
    template_name = "manage/lists/payment.html"
    model = Payment