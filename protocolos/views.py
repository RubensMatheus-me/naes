from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import (Category, Product, Review, Stock, Cart, CartProduct, Order, OrderProduct, Payment)



class PaginaInicial(LoginRequiredMixin, TemplateView):
    template_name = 'manager.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.order_by("-id")[:5]
        context["latest_orders"] = Order.objects.filter(user=self.request.user).order_by("-date")[:5]
        return context

# -----------------------------
# Create Views
# -----------------------------

class CategoryCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = Category
    fields = ["name", "description"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Cadastrar Categoria"}


class ProductCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = Product
    fields = ["name", "description", "price", "size", "color", "category", "image"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Cadastrar Produto"}


class ReviewCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = Review
    fields = ["product", "rating", "description"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Cadastrar Avaliação"}

    def form_valid(self, form):
        form.instance.user = self.request.user

        url = super().form_valid(form)

        return url


class StockCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = Stock
    fields = ["product", "quantity"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Cadastrar Estoque"}


class CartCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = Cart
    fields = ["user", "total_price"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Cadastrar Carrinho"}


class CartProductCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = CartProduct
    fields = ["cart", "product", "quantity"]
    success_url = reverse_lazy("manage")   
    extra_context = {"title": "Cadastrar Produto no Carrinho"}


class OrderCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = Order
    fields = ["user", "status", "delivery_address", "total_price"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Cadastrar Pedido"}


class OrderProductCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = OrderProduct
    fields = ["order", "product", "quantity"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Cadastrar Produto no Pedido"}


class PaymentCreate(LoginRequiredMixin, CreateView):
    template_name = "manage/form-add.html"
    model = Payment
    fields = ["order", "payment_method", "payment_status", "value"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Cadastrar Pagamento"}


# -----------------------------
# Update Views
# -----------------------------

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = Category
    fields = ["name", "description"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Editar Categoria"}


class ProductUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = Product
    fields = ["name", "description", "price", "size", "color", "category", "image"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Editar Produto"}


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = Review
    fields = ["user", "product", "rating", "description"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Editar Avaliação"}


class StockUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = Stock
    fields = ["product", "quantity"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Editar Estoque"}


class CartUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = Cart
    fields = ["user", "total_price"]
    success_url = reverse_lazy("manage")   
    extra_context = {"title": "Editar Carrinho"}


class CartProductUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = CartProduct
    fields = ["cart", "product", "quantity"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Editar Produto do Carrinho"}


class OrderUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = Order
    fields = ["user", "status", "delivery_address", "total_price"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Editar Pedido"}


class OrderProductUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = OrderProduct
    fields = ["order", "product", "quantity"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Editar Produto do Pedido"}


class PaymentUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manage/form-add.html"
    model = Payment
    fields = ["order", "payment_method", "payment_status", "value"]
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Editar Pagamento"}


# -----------------------------
# Delete Views
# -----------------------------

class CategoryDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = Category
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Excluir Categoria"}


class ProductDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = Product
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Excluir Produto"}


class ReviewDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = Review
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Excluir Avaliação"}


class StockDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = Stock
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Excluir Estoque"}


class CartDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = Cart
    success_url = reverse_lazy("manage")  
    extra_context = {"title": "Excluir Carrinho"}


class CartProductDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = CartProduct
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Excluir Produto do Carrinho"}


class OrderDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = Order
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Excluir Pedido"}


class OrderProductDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = OrderProduct
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Excluir Produto do Pedido"}


class PaymentDelete(LoginRequiredMixin, DeleteView):
    template_name = "manage/form-delete.html"
    model = Payment
    success_url = reverse_lazy("manage")
    extra_context = {"title": "Excluir Pagamento"}


# -----------------------------
# List Views
# -----------------------------

class CategoryList(LoginRequiredMixin, ListView):
    template_name = "lists/category.html"
    model = Category


class ProductList(LoginRequiredMixin, ListView):
    template_name = "lists/product.html"
    model = Product


class ReviewList(LoginRequiredMixin, ListView):
    template_name = "lists/review.html"
    model = Review


class StockList(LoginRequiredMixin, ListView):
    template_name = "lists/stock.html"
    model = Stock


class CartList(LoginRequiredMixin, ListView):
    template_name = "lists/cart.html"
    model = Cart


class CartProductList(LoginRequiredMixin, ListView):
    template_name = "lists/cart_product.html"
    model = CartProduct


class OrderList(LoginRequiredMixin, ListView):
    template_name = "lists/order.html"
    model = Order


class OrderProductList(LoginRequiredMixin, ListView):
    template_name = "lists/order_product.html"
    model = OrderProduct


class PaymentList(LoginRequiredMixin, ListView):
    template_name = "lists/payment.html"
    model = Payment