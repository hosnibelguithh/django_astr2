"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from accounts.views import HomeView, agents_list, register, login_view,DashboardView,ProfileUpdateView,ProfileView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),

    path('register/',register, name='register'),

    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
        ),
        name='logout'
    ), 
     path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('agents/',agents_list, name='agents'),

    path('leads/',  include('leads.urls', namespace="leads")),
   
 ]

