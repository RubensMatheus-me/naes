from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View

from protocolos.models import Product, Order

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = 'paginasweb/modelos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome"] = "Rubens Matheus"
        context['latest_products'] = Product.objects.all().order_by('-id')[:5]

        if self.request.user.is_authenticated:
            context["latest_orders"] = Order.objects.filter(user=self.request.user).order_by("-date")[:5]
        else:
            context["latest_orders"] = []
        return context

class SobreView(TemplateView):
    template_name = "paginasweb/sobre.html"
 
 