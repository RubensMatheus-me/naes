import django_filters
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Nome do Produto')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Categoria')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Preço Mínimo')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Preço Máximo')
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'price_min', 'price_max']

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Nome da Categoria')

    class Meta:
        model = Category
        fields = ['name']