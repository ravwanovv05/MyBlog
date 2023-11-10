from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db.models import Q
from django.contrib import messages

User = get_user_model()


class RegisterView(View):
    template_name = "register.html"

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(Q(email=email)).exists():
                messages.error(request, 'This email already exists!')
                return redirect('/')
            if User.objects.filter(Q(username=username)).exists():
                messages.error(request, 'This username already exist!')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password
                )
                user.save()
                return redirect('/')
        else:
            messages.error(request, 'Passwords are not same!')
            return redirect('/')


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('/login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
