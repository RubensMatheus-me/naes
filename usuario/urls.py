from django.urls import path
from .views import AjaxLoginView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path("login/", AjaxLoginView.as_view(), name="login"),  # Aqui já está correto
    path("logout/", LogoutView.as_view(), name="logout"),  # Parênteses faltando
    path("change-password/", PasswordChangeView.as_view(
        template_name="manage/form-add.html",
        extra_context={"titulo": "Alterar Senha"}), name="change-password")
]
