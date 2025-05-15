# urls.py
from django.urls import path

from .views import (CategoryCreate, ProductCreate, ReviewCreate, StockCreate, CartCreate, CartProductCreate, OrderCreate, OrderProductCreate, PaymentCreate)
from .views import (CategoryUpdate, ProductUpdate, ReviewUpdate, StockUpdate, CartUpdate, CartProductUpdate, OrderUpdate, OrderProductUpdate, PaymentUpdate)
from .views import (CategoryDelete, ProductDelete, ReviewDelete, StockDelete, CartDelete, CartProductDelete, OrderDelete, OrderProductDelete, PaymentDelete)
from .views import (CategoryList, ProductList, ReviewList, StockList, CartList, CartProductList, OrderList, OrderProductList, PaymentList,)

urlpatterns = [

    path("cadastrar/categoria/", CategoryCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/produto/", ProductCreate.as_view(), name="cadastrar-produto"),
    path("cadastrar/avaliacao/", ReviewCreate.as_view(), name="cadastrar-avaliacao"),
    path("cadastrar/estoque/", StockCreate.as_view(), name="cadastrar-estoque"),
    path("cadastrar/carrinho/", CartCreate.as_view(), name="cadastrar-carrinho"),
    path("cadastrar/produto-no-carrinho/", CartProductCreate.as_view(), name="cadastrar-produto-carrinho"),
    path("cadastrar/pedido/", OrderCreate.as_view(), name="cadastrar-pedido"),
    path("cadastrar/produto-no-pedido/", OrderProductCreate.as_view(), name="cadastrar-produto-pedido"),
    path("cadastrar/pagamento/", PaymentCreate.as_view(), name="cadastrar-pagamento"),

    path("editar/categoria/<int:pk>/", CategoryUpdate.as_view(), name="editar-categoria"),
    path("editar/produto/<int:pk>/", ProductUpdate.as_view(), name="editar-produto"),
    path("editar/avaliacao/<int:pk>/", ReviewUpdate.as_view(), name="editar-avaliacao"),
    path("editar/estoque/<int:pk>/", StockUpdate.as_view(), name="editar-estoque"),
    path("editar/carrinho/<int:pk>/", CartUpdate.as_view(), name="editar-carrinho"),
    path("editar/produto-no-carrinho/<int:pk>/", CartProductUpdate.as_view(), name="editar-produto-carrinho"),
    path("editar/pedido/<int:pk>/", OrderUpdate.as_view(), name="editar-pedido"),
    path("editar/produto-no-pedido/<int:pk>/", OrderProductUpdate.as_view(), name="editar-produto-pedido"),
    path("editar/pagamento/<int:pk>/", PaymentUpdate.as_view(), name="editar-pagamento"),

    path("excluir/categoria/<int:pk>/", CategoryDelete.as_view(), name="excluir-categoria"),
    path("excluir/produto/<int:pk>/", ProductDelete.as_view(), name="excluir-produto"),
    path("excluir/avaliacao/<int:pk>/", ReviewDelete.as_view(), name="excluir-avaliacao"),
    path("excluir/estoque/<int:pk>/", StockDelete.as_view(), name="excluir-estoque"),
    path("excluir/carrinho/<int:pk>/", CartDelete.as_view(), name="excluir-carrinho"),
    path("excluir/produto-no-carrinho/<int:pk>/", CartProductDelete.as_view(), name="excluir-produto-carrinho"),
    path("excluir/pedido/<int:pk>/", OrderDelete.as_view(), name="excluir-pedido"),
    path("excluir/produto-no-pedido/<int:pk>/", OrderProductDelete.as_view(), name="excluir-produto-pedido"),
    path("excluir/pagamento/<int:pk>/", PaymentDelete.as_view(), name="excluir-pagamento"),

    path("listar/categorias/", CategoryList.as_view(), name="listar-categoria"),
    path("listar/produtos/", ProductList.as_view(), name="listar-produto"),
    path("listar/avaliacoes/", ReviewList.as_view(), name="listar-avaliacao"),
    path("listar/estoques/", StockList.as_view(), name="listar-estoque"),
    path("listar/carrinhos/", CartList.as_view(), name="listar-carrinho"),
    path("listar/produtos-no-carrinho/", CartProductList.as_view(), name="listar-produto-carrinho"),
    path("listar/pedidos/", OrderList.as_view(), name="listar-pedido"),
    path("listar/produtos-no-pedido/", OrderProductList.as_view(), name="listar-produto-pedido"),
    path("listar/pagamentos/", PaymentList.as_view(), name="listar-pagamento"),
]
