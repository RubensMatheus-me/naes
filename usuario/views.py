
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
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

class RegisterView(TemplateView):
    template_name = "manage/form-add.html"

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "As senhas não coincidem.")
            return redirect("login")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Este nome de usuário já está em uso.")
            return redirect("login")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está em uso.")
            return redirect("login")

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)  
        messages.success(request, "Registro realizado com sucesso!")
        return redirect("/")