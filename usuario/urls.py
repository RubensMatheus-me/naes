from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name = "manage/form-add.html",
        extra_context={"titulo": "Autenticação"}, next_page="/"), name="login"),
    
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path("alterar-senha/", PasswordChangeView.as_view(
        template_name="protocolos/form.html",
        extra_context={"titulo": "Alterar minha senha"}), name="alterar-senha"),
]
