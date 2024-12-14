from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User, Group


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Неверные данные для входа", status=401)
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponse("Вы успешно вышли из системы")


@login_required
def user_data_view(request):
    user = request.user
    return HttpResponse(f"Вы авторизованы как: {user.username}, email: {user.email}")


def add_superusers_to_group():
    group = Group.objects.get(name='UserManagement')
    superusers = User.objects.filter(is_superuser=True)
    for superuser in superusers:
        superuser.groups.add(group)
        print(f"Суперпользователь {superuser.username} добавлен в группу {group.name}.")
