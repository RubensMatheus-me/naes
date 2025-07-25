
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User

class LoginView(View):
    template_name = "manage/form-add.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        identifier = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=identifier, password=password)

        if not user:
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass

        if user is not None:
            login(request, user)
            return redirect("/") 
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect("login")

class RegisterView(View):
    template_name = "manage/form-add.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"titulo": "Registrar"})

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmed_password = request.POST.get("confirmedPassword")

        if not username or not email or not password or not confirmed_password:
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect("login")

        if password != confirmed_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("login")

        if len(password) < 6:
            messages.error(request, "A senha deve ter pelo menos 6 caracteres.")
            return redirect("login")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já está em uso.")
            return redirect("login")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email já cadastrado.")
            return redirect("login")

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Cadastro realizado com sucesso! Você está logado.")
        return redirect("/")
