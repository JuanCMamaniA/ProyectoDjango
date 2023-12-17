from django.shortcuts import render

#======================
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

#======================


def casa(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def registro_user(request):
    return render(request, 'registro_user.html')




#logout =============

def custom_logout(request):
    logout(request)
    return redirect('/index')

#logout =============


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html') 

    return render(request, 'login.html')



