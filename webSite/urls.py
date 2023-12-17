"""
URL configuration for webSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


from django.views.generic import RedirectView
from myproyect import views
from django.contrib.auth import views as auth_views


from myproyect.views import (   
    login,
    registro_user,
    perfil,
    )
   


from myproyect import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.casa,name='casa'),

    # login, perfil , registro_user
    path('', RedirectView.as_view(url='index/', permanent=False)),     
    path('', login, name='login'),    
    path('perfil.html', perfil, name='perfil'),
    path('registro_user/', registro_user, name='registro_user'), 
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),

  


]
